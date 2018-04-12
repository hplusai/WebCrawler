# coding=utf-8
import lxml
import lxml.html
import SmartTypes
from lxml.cssselect import CSSSelector
from lxml import etree
import tempfile
import utils.fileutils
import utils,sys, md5
from utils import app
from utils import fileutils as fsys
from utils import threads
from utils.fileutils import Save2File,GetFileData,GetTempFilename
import utils.SmartTypes
from utils.SmartTypes import SmartDict
import operator as op,os, re
import requests, httplib
import HTMLParser
import certifi
#import spynner
#import mechanize
#from mechanize import HTTPRedirectHandler,HTTPEquivProcessor,HTTPRefreshProcessor,HTTPRefererProcessor#HTTPCookieProcessor,

import socket,urllib,urllib2, cookielib
urllib2.socket.setdefaulttimeout(30)
socket.setdefaulttimeout(60)

import thread,threading,traceback
import uuid
import urlparse
from urlparse import urljoin, urlsplit, parse_qs
import time, random, StringIO, subprocess
import proxies
import imghdr
import chardet

redirect_re = re.compile('<meta[^>]*?url=(.*?)["\']', re.IGNORECASE)

#DefEnc='utf-8'
from app import local

WebSiteEncoding=app.UnpickleObj('web_enc.obj') or {}

def DocCheck(s):
    sl=s.lower()
    ret=0
    try:
        if '<html' not in sl:
            return 0
        if '</html>' not in sl:
            return 0

        if len(sl)<1000:
            return 0

        if AdditionalDocCheck:
            if not AdditionalDocCheck(sl):
                return 0
        ret=1
        return ret
    finally:
        if not ret:
            # обнуляем прокси и куки
            cf=getattr('local','CookieFile','None')
            if cf and os.path.exists(cf):
                os.remove(local.CookieFile)
                local.CookieFile=None
                local.GoodProxy=None


cacheLocation=app.AbsPath('cache')
if not os.path.exists(cacheLocation):
    os.mkdir(cacheLocation)

def StdCacheUrl(url,RemovePars=[]):
    url=url.lower()
    spl=urlsplit(url)
    pars=parse_qs(spl[-2],1,0)
    pars=[k+'='+','.join(v) for k,v in pars.items() if k not in RemovePars]
    pars.sort()
    spars='&'.join(pars)
    nUrl='$$'.join(list(spl[1:-2])+[spars])
#    nFile=app.FileNameFromStr(nUrl)
    nFile=fsys.removeDisallowedFilenameChars(nUrl)
    return nFile

AutoFixLinks=getattr(app.params,'AutoFixLinks',1)

GlobalDocCorrect=getattr(app.params,'DocCheck',DocCheck)
AdditionalDocCheck=getattr(app.params,'AdditionalDocCheck',None)
onFormatCacheUrl=getattr(app.params,'onFormatCacheUrl',StdCacheUrl)

EnableCache=getattr(app.params,'EnableCache',1)
OnlyCache=getattr(app.params,'OnlyCache',0)
flRebuildCache=getattr(app.params,'RebuildCache',1)

CurlTimeOut=getattr(app.params,'TimeOut',13)
CurlConnectTimeOut=getattr(app.params,'ConnectTimeOut',5)
LinksLimit=getattr(app.params,'LinksLimit',10000)
NoErrorsMode=getattr(app.params,'NoErrorsMode',0)
UrlGetDelay=getattr(app.params,'UrlGetDelay',0)
UseSsl=getattr(app.params,'UseSsl',1)

UseCurl=getattr(app.params,'UseCurl',0)
RegErrors=(IOError,)
if UseCurl:
    import curl
    RegErrors=(IOError, curl.pycurl.error)

UseSpynner=getattr(app.params,'UseSpynner',0)
if UseSpynner:
    import spynner
    from spynner import browser
    SpynnerShowRule=getattr(app.params,'SpynnerShowRule',None)
    SpynnerUseJs=getattr(app.params,'SpynnerUseJs',1)

Threads4Parse=getattr(app.params,'Threads4Parse',0)
Thread_RepeatIfExcept=getattr(app.params,'Thread_RepeatIfExcept',3)

ProxyFunc=None # must return proxy on demand

def DoUseProxies(ProxiesUrlsOrLocalFiles=[]):
    global ProxyFunc
    map(proxies.AddProxiesList,ProxiesUrlsOrLocalFiles)
    ProxyFunc=proxies.GetProxy

Proxies=getattr(app.params,'Proxies',[])
if Proxies:
    DoUseProxies(Proxies)

def GetUrlWebSite(Url):
    parsed_uri = urlparse.urlparse(Url)
    domain = '{}://{}/'.format(parsed_uri[0], parsed_uri[1])
    return domain

def css(s,sAddPath=''):
    ret = CSSSelector(s)
    return ret.path+sAddPath

def FixLinks(d):
    n=xNodes(d,'.//a')
    for x in n:
        href=x.attrib.get('href','').strip()
        if href<>'' and href<>'#' and not href.lower().startswith('javascript:'):
            np=urljoin(local.sHostName,href)
            try:
                x.attrib['href']=np
            except:
                print('FixLinks error : ',np)

def Div(Html,Class=''):
    return '<div class="%s">'%Class+Html+'</div>'

def WebFormPost(url,PostParams={},frmFilter=None,checkForLogin=0, flJustGetActParams=0, flNoError=0):
    if isinstance(url,(basestring)):
        d=GetXDoc(url)
    else:
        d=url
    keys=PostParams.keys()
    frmLoginRule=' and '.join(map(lambda x: 'count(.//*[@name="%s"])>0'%x,keys))
    LoginForm='.//form[%s]'%frmLoginRule
    frms=xNodes(d,LoginForm)
    if not frms:
        if checkForLogin:
            return d
        else:
            if not flNoError:
                raise Exception('WebFormPost. Cannot find form')
            else:
                return None
    frm=filter(lambda x: not frmFilter or len(xNodes(x,frmFilter))>=1,frms)[0]
    act=xValue(frm,'@action')
    method=xValue(frm,'@method').lower().strip()
    r=ParseXDoc(frm,{'.//*[@name!=""]':['@name','@value']})
    r=app.ArrTree2OneDimArr(r)
    r=filter(lambda x : x[0]!='',r)
    r=SmartTypes.SmartDict(r)

    # remove None Items
    for k,v in PostParams.items():
        if v is None:
            del PostParams[k]

    r.update(PostParams)

    if method=='get':
        act+='?'+urllib.urlencode(r)
        r=None

    if flJustGetActParams:
        return act,r

    doc=GetXDoc(act,postParams=r)

    if checkForLogin and xNodes(doc,LoginForm):
        raise BaseException('Login Error')
    return doc

def WebLogin(url,PostParams={},frmFilter=None ):
    return WebFormPost(url,PostParams,frmFilter,checkForLogin=1)

def GetCharset(data,defenc='utf-8'):
    ret=re.findall("""<meta.*?charset=([^"']+)""",data,re.IGNORECASE)
    if not ret:
        ret=re.findall("""encoding=([^"']+)""",data,re.IGNORECASE)
    if not ret:
        return defenc
    return ret[0]

MsWordLock=app.AllocLock()
flUseExistCurl=False
CookieFile=None#app.AbsPath('curl.cookies')
cookiesLocation='cookies'
if not os.path.exists(app.AbsPath(cookiesLocation)):
    os.mkdir(app.AbsPath(cookiesLocation))

#DetectedEncoding=None
flNoEncDec=1

#--bugfix
def FreeAndNil(doc):
    try:
        doc.free()
        doc=None
    except:
        pass

def DetectFileEnc(fName, DefEncRes='utf-8'):
    cd=chardet.detect(GetFileData(fName))
    return (cd and cd['encoding']) or DefEncRes

def cReq(proxy=None):
    global local

    if ProxyFunc and (not proxy or proxy.strip()==''):
        app.Log('cReq. NO PROXY CALL','ERROR.log')

    if flUseExistCurl:
        if not hasattr(local,'fcReq'):
            ret=local.fcReq=curl.Curl()
        else:
            return local.fcReq
    else:
        ret=curl.Curl()

    ret.set_option(curl.pycurl.USERAGENT,'Mozilla/5.0 (Windows; U; Windows NT 5.2; ru; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
    ret.set_option(curl.pycurl.FOLLOWLOCATION,True)

    if proxy:
        lProx=proxy.strip().split(':')
        ps,pp=lProx[:2]
        ret.set_option(curl.pycurl.PROXY, ps)
        ret.set_option(curl.pycurl.PROXYPORT, int(pp))
        if len(lProx)==4:
            ret.set_option(curl.pycurl.PROXYUSERPWD, '%s:%s'%tuple(lProx[2:]))

    if local.CookieFile:
        ret.set_option(curl.pycurl.COOKIEJAR,local.CookieFile)
        ret.set_option(curl.pycurl.COOKIEFILE,local.CookieFile)

    if UseSsl:
        ret.set_option(curl.pycurl.CAINFO, app.AbsPath('ca-bundle.crt'))
        ret.set_option(curl.pycurl.SSLCERT, app.AbsPath('cacert.pem'))
        ret.set_option(curl.pycurl.CAPATH,app.AbsPath('/'))
        ret.set_option(curl.pycurl.SSLVERSION, 3)
        ret.set_option(curl.pycurl.SSLCERTTYPE,'PEM')
        ret.set_option(curl.pycurl.SSL_VERIFYPEER, 1)
        ret.set_option(curl.pycurl.SSL_VERIFYHOST, 2)
#        ret.set_option(curl.pycurl.SSL_VERIFYPEER, False)
#        ret.set_option(curl.pycurl.SSL_VERIFYHOST, False)
#        ret.set_option(curl.pycurl.SSLVERSION_SSLv3, 1)

    #ret.set_option(curl.pycurl.HTTPHEADER,("Accept: text/plain",))
    ret.set_timeout(CurlTimeOut)
    ret.set_option(curl.pycurl.CONNECTTIMEOUT, CurlConnectTimeOut)
    return ret

##RuEncoding='latin_1'

def GetUrlSize(Url,proxy=None):
    return GetUrlInfo(Url,proxy)['content-length-download']

def GetUrlInfo(Url,proxy=None):
    return cReq(proxy).just_info(DoNormUrl(Url))

def BasicAuthAndGetPages(rooturl='http://192.168.1.1',username='admin',password='admin',urls=[]):
    # set root url
    DoNormUrl(rooturl)
    # create a urllib2 opener for basic authentication
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, rooturl, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    return map(lambda url : urllib2.urlopen(DoNormUrl(url)).read(),urls)

def EncRus(Text):
    if not flNoEncDec:
        return Text

    if isinstance(Text,unicode):
        return Text.encode('utf-8')

    return Text

def DecRus(Text):
    if not flNoEncDec:
        return Text

    if isinstance(Text,unicode):
        return Text

    return Text.decode('utf-8')

test_new_urlget=0

def cache(flEnable,flRebuild=0):
    global EnableCache,flRebuildCache
    EnableCache=flEnable
    flRebuildCache=flRebuild

def GetDefCookieFile(url,pProxy):
    NewCookieExt=''
    if pProxy:
        NewCookieExt='.'+pProxy.split(':')[0]+'.cookies'
#        cookiesLocation
    DefCookieFile=CookieFile and ((NewCookieExt and fsys.StrChangeFileExt(CookieFile,NewCookieExt.strip('.'))) or CookieFile)
    DefCookieFile=DefCookieFile or (GetUrlWebSite(url).strip('https://').strip('http://').strip('/')+(NewCookieExt or '.cookies'))
    DefCookieFile=cookiesLocation+'/'+DefCookieFile
    app.Log('Cookie='+app.AbsPath(DefCookieFile))
    return app.AbsPath(DefCookieFile)


def GetUrlData(Url,proxy=None, postParams=None):
    """
      postParams=SmartTypes.SmartDict
    """
    local.sHostName=getattr(local,'sHostName','') or Url
    local.LastUsedProxy=None
    local.IsDocCorrect=getattr(local,'IsDocCorrect',GlobalDocCorrect)

    def UrlGet(sUrl, pProxy, pPostParams=None):
        Req=None
        ret=''
        try:
            local.ProxyFunc=getattr(local,'ProxyFunc',ProxyFunc)
            pProxy=local.LastUsedProxy=(pProxy or getattr(local,'GoodProxy',None) or (local.ProxyFunc and local.ProxyFunc()))
            local.CookieFile=getattr(local,'CookieFile',GetDefCookieFile(url,pProxy))

            if UseCurl:
            # !! Curl just great but problems with SSL and problems with deploying on Custom soft etc (android) - NOT NATIVE urllib2 much better only one problem with proxies
                Req=cReq(pProxy)

                if pPostParams:
                    ret=Req.post(sUrl,pPostParams)
                else:
                    ret=Req.get(sUrl)
            elif UseSpynner:
#                print('spynner.Browser')
                if Threads4Parse>0:
                    raise Exception('spynner.Browser works in 1 Thread Only')
                sCookies=''
                if os.access(local.CookieFile, os.F_OK):
                    with open(local.CookieFile,'rb') as f:
                        sCookies=f.read()
                def get_data(b):
                    if isinstance(b, file):
                        h = b.read()
                    if isinstance(b, browser.Browser):
                        h = str(b.webframe.toHtml())
                    if not isinstance(h, basestring):
                        h = str(b)
                    app.local.data_ret=h
                    return 1

                if getattr(local,'browser',None) is None:
                    local.browser=spynner.Browser(user_agent='Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.8.131 Version/11.10')

                b=local.browser

                b.set_cookies(sCookies)
                if pProxy:
                    b.set_proxy(pProxy)

                if SpynnerUseJs:
                    b.load(sUrl, load_timeout=CurlTimeOut)
                    b.wait_for_content(get_data, 2)
                    b.load_jquery(True)
                    if SpynnerShowRule and SpynnerShowRule(local.data_ret):
                        b.create_webview()
                        b.webview.show()
                        while b.webview:
                            b._events_loop()
                    try:
                        ret=local.data_ret
                        sCookies=b.cookiesjar.mozillaCookies()
                        with open(local.CookieFile,'w') as f:
                            f.write(sCookies)
                        #b.close()
                        #b=None
                    except:
                        app.LogError()
                else:
                    ret=b.download(sUrl,proxy_url=pProxy)
                    return ret
            else:
                #'https://www.google.com/'
                if getattr(local,'cj',None) is None:
                    local.cj = cookielib.MozillaCookieJar(local.CookieFile)
                    if not pProxy and os.access(local.CookieFile, os.F_OK):
                        local.cj.load(ignore_discard=True)

                r = requests.request(url=sUrl,headers={'User-agent': 'Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.8.131 Version/11.10'},method=(pPostParams and 'POST') or 'GET',params=pPostParams,cookies=local.cj,timeout=CurlTimeOut,allow_redirects=True,proxies=(pProxy and {'http': pProxy}) or None, verify=True)#,'https':pProxy,'ftp':pProxy
                return r.content
            # ! urllib2 seems threadsafe but work worst with proxy
            return ret
        finally:
            if UseCurl and not flUseExistCurl and Req:
                Req.close()
                Req=None

    def OnError(e=None):
        if local.LastUsedProxy:
            local.GoodProxy=None

        if ProxyFunc:
            proxies.AddProxy2BlackList(local.LastUsedProxy)

#---------------------------------------------------------------------
    url=DoNormUrl(Url)

    try:
        cacheFile=''
        if EnableCache:
            urlCache=url
            if onFormatCacheUrl:
                hash=onFormatCacheUrl(url)
            else:
            	hash = md5.new(urlCache).hexdigest()
            cacheFile=cacheLocation + "/" + hash + ".html"
            if os.path.exists(cacheFile) and not flRebuildCache:# and not postParams:
                ret=GetFileData(cacheFile,0,'rb')
            else:
                # collect info only from cached files
                if OnlyCache:
                    raise Exception('!WARNING CACHE ONLY MODE; url : %s is not cached'%url)
                ret=UrlGet(url,proxy,postParams)
                fsys.Save2File(cacheFile, ret,'wb')

                # delay
                if UrlGetDelay:
                    time.sleep(UrlGetDelay)

                # FULL LOG
                if 0:
                    if not os.path.exists(cacheLocation+r'/all'):
                        os.mkdir(cacheLocation+r'/all')
                    fsys.Save2File(cacheLocation + "/all/" + hash + ".html", ret,'wb')
    #                    app.Log(url+'='+hash,"cache.hist")
        else:
            ret=UrlGet(url,proxy,postParams)
            # delay
            if UrlGetDelay:
                time.sleep(UrlGetDelay)

        # additional check, probably that's an image
        if not imghdr.what(None,ret[:32]):
            if local.IsDocCorrect and not local.IsDocCorrect(ret):
                if cacheFile<>'':
                    try:
                        os.remove(cacheFile)
                    except:
                        pass
                raise Exception('IsDocCorrect Failed :Url= %s \n %s'%(url,ret))

        if 'Bad Request' in ret and len(ret)<500:
            raise Exception('Bad Request '+ url)

        if local.LastUsedProxy:
            local.GoodProxy=local.LastUsedProxy
            if ProxyFunc:
                proxies.AddProxy2GoodList(local.LastUsedProxy)

        return ret
    except RegErrors:
        OnError()
        app.LogError('GetUrlData. Except.',1,'proxy_errors.log')
    except:
        OnError()
        app.LogError('GetUrlData. Except.',(not NoErrorsMode and 1) or 0)
        if NoErrorsMode:
            return ''

def GetXDocFromData(Data,Encoding=None):
    #auto detect and remove xmlns
    #<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" # lang="ru">
    if 'xmlns=' in Data:
        Data=Data.replace('xmlns=','this_xmlns_was_removed_case_libxml2=')

    Encoding=Encoding or GetCharset(Data) #GetWebSiteEncoding(None,Data)

    try:
        #ret=libxml2.htmlParseDoc(Data,Encoding)
        parser = etree.HTMLParser()
        #(isinstance(Data,unicode) and Data) or Data.decode(Encoding))
        #or ' charset="utf' in Data
        if (not isinstance(Data,unicode)):
            enc=GetCharset(Data)
            Data=Data.decode(enc)
        ret = etree.parse(StringIO.StringIO(Data), parser)
        if AutoFixLinks:
            FixLinks(ret)
    except:
        app.LogError(Data,1,'libxml_error.log')

    return ret

def GetXDoc(Url,Proxy=None, postParams=None):
    app.Log('GetXDoc('+Url+')')
    if proxies.IsUrl(Url):
        Data=GetUrlData(Url, Proxy, postParams)
    else:
        Data=GetFileData(Url)
        enc=GetCharset(Data,None)
        if enc:
            Data=GetFileData(Url,Encoding=enc)

    if not Data or Data.strip()=='':
        app.Log('Exception : NO DATA in GetXDoc','ERROR.log')
        return None

    return GetXDocFromData(Data)

def GetXDocFromXml(FileName):
    parser = etree.XMLParser()
    ret = etree.parse(FileName, parser)
    return ret

def GetXDocFromWord(Url):
    from win32com.client import DispatchWithEvents, Dispatch
    Data=GetUrlData(urllib2.unquote(Url))
    docName=GetTempFilename('.doc');
    Save2File(docName,Data,'wb')
    # only one Ms word document (no multithreads)
    MsWordLock.acquire()
    try:
        import pythoncom
        pythoncom.CoInitialize()
        word = Dispatch("Word.Application")
        word.Visible=1
        doc=word.Documents.Open(docName,Revert=1,Visible=0,OpenAndRepair=1)
        htmName=GetTempFilename('.htm');
        word.ActiveDocument.SaveAs(htmName,8);
        doc.Close()
    finally:
        MsWordLock.release()
    return GetXDoc(htmName)

def SmartXpath(Node,xPath):
    DecXPath=DecRus(xPath.replace('->','following-sibling::node()[1]').replace('<-','preceding-sibling::node()[1]'))
    try:
      return Node.xpath(DecRus(DecXPath))
    except:
        app.LogError('SmartXpath.'+DecXPath,1)

def xNodes(Node,xPath, CheckCount=0):
    ret=SmartXpath(Node,xPath)
    if (CheckCount>0) and (len(ret)<>CheckCount):
        err='CorrectCount=%s;\nMatches.Count=%s;\nXPath=%s;\nurl=%s'%(CheckCount, len(ret),xPath,GetDocUrl(Node))
        app.Log(err,'Wrong_matches_count.log')
        if NoErrorsMode:
            ret=[None]*CheckCount
        else:
            raise BaseException(err)
    return ret

def xNode(Node,xPath, flRaise=1):
    ret=xNodes(Node,xPath,flRaise)
    if len(ret)<>1:
        return None
    return ret[0]

def xNodeContent(node,fltRemove=''):
    if not hasattr(node,'itertext'):
        return unicode(node)

    if fltRemove:
        l=xNodes(node,fltRemove)
        zzz=[x.getparent().remove(x) for x in l]

    l=node.itertext()
    if l is None:
        return ''

    l=list(l)

    if not l:
        return ''

    return ''.join(l)

def xText(node):
    s=lxml.etree.tostring(node,with_tail=False)
    for n in node.getchildren():
        sr=lxml.etree.tostring(n,with_tail=False)
        s=s.replace(sr,'')
    sRet=lxml.etree.XML(s)
    return sRet.text

def xValues(Node,xPath, CheckCount=0,flEncode=1,subPathes=[]):
    ret=xNodes(Node,xPath, CheckCount)
    return map(lambda x:(flEncode and EncRus(xNodeContent(x))) or xNodeContent(x),ret)

def xValue(Node,xPath='.', flRaise=1,Default='',flEncode=1):
    ret=xValues(Node,xPath, flRaise, flEncode)
    return (ret and ret[0]) or Default

#def xProps(Node):
#    return SmartDict([[x.name,xNodeContent(x)] for x in Node.properties if x.type=='attribute'])

def xHtmls(Node,xPath, CheckCount=0,flEncode=1,subPathes=[]):
    ret=xNodes(Node,xPath, CheckCount)
    ret=[((x is not None) and lxml.html.tostring(x,pretty_print=True,encoding='utf-8',with_tail=False)) or '' for x in ret]
    return map(lambda x:(flEncode and EncRus(x)) or x,ret)

def xHtml(Node,xPath='.', flRaise=1,Default='',flEncode=1):
    ret=xHtmls(Node,xPath, flRaise, flEncode)
    return (ret and ret[0]) or Default

def xInnerHtml(Node,xPath='.', Default='',flEncode=1):
    ret=''.join(xHtmls(Node,xPath+'/*', 0, flEncode))
    return ret

def xAbsPath(n):
    return (n is not None and n.getroottree().getpath(n)) or ''

def DoNormUrl(url, defHost=''):
    url=url.strip()
    local.sHostName=getattr(local,'sHostName',defHost)
    local.sHostName=urljoin(local.sHostName, url)
    return local.sHostName

class gUrl():
    """Evaluate Xpath or function for current doc, open value (Url) as next level doc
IMPORTANT!!! First function param Document.
if CheckCount<>0"""
    def __init__(self,xpathOrFunc, flRaiseIfNotFound=1):
        self.xpathOrFunc=xpathOrFunc
        self.flRaiseIfNotFound=flRaiseIfNotFound

    def __call__(self,doc):
        xp=app.CallOrReturn(self.xpathOrFunc)
        r=xValues(doc,xp)

        # raise error
        if not r and self.flRaiseIfNotFound:
            return xValue(doc,xp,1)

        return [UrlSaveGetXDoc(v,doc) for v in r]

class gContent():
    """Evaluate Xpath or function for current doc,and return serialized value for node
IMPORTANT!!! First function param Document."""
    def __init__(self,xpathOrFunc,enc='utf8'):
        self.xpathOrFunc=xpathOrFunc
        self.enc=enc

    def __call__(self,doc):
        node=xNode(doc,app.CallOrReturn(self.xpathOrFunc))
        return lxml.html.tostring(node,pretty_print=True)

class gConst():
    """just return const value
"""
    def __init__(self,val):
        self.val=val

    def __call__(self,doc):
        return self.val

def gFileAutoNaming(doc,iUrl):
    tmpDir=app.AbsPath('temp')
    fsys.CreateDirs(tmpDir)
    return GetTempFilename(dir=tmpDir)

class gFile():
    """Evaluate Xpath or function for current doc and return list of filenames saved to disk
Also you can use custom defined function for filenames,
in other case temp filenames
IMPORTANT!!! First function param Document."""
    def __init__(self,xpathOrFunc,fname=gFileAutoNaming):
        self.xpathOrFunc=xpathOrFunc
        self.fname=fname
#        self.enc=enc

    def __call__(self,doc):
        if callable(self.xpathOrFunc):
            iUrl=self.xpathOrFunc(doc)
        else:
            iUrl=xValue(doc,self.xpathOrFunc)
        fname=app.CallOrReturn(self.fname,doc,iUrl)
        if not(EnableCache and os.path.exists(fname)):
            Save2File(fname,GetUrlData(iUrl),'wb')
        return fname

def GetDocUrl(CurDoc):
    return ((not IsEmpty(CurDoc)) and ((hasattr(CurDoc,'getroottree') and CurDoc.getroottree()) or CurDoc).getroot().get('docurl')) or ''

def UrlSaveGetXDoc(Url,CurDoc=None):
    if Url=='':
        return None

    doc=None

    ## we will open only LinksLimit urls.
    local.LinksLimit=getattr(local,'LinksLimit',LinksLimit)
    if not local.LinksLimit:
        return doc
    local.LinksLimit-=1

    local.sHostName=GetDocUrl(CurDoc) or getattr(local,'sHostName','')
    try:
        doc=GetXDoc(Url)
        app.Log("UrlSaveGetXDoc.local.sHostName=%s"%local.sHostName)
        doc.getroot().set('docurl',app.EncodeStrings(local.sHostName,'unicode'))
    except:
        app.LogError(Url,(not NoErrorsMode and 1) or 0)

    return doc

def ParseAndSaveXDoc(UrlOrFNameOrDoc, xPaths, StoreFunc=None, IsDocCorrect=None):
    """
    parse doc and links in there by parameters
test=ParseAndSaveXDoc('http://www.mmk-metiz.ru/content/prices/products',
               {'.//div/dt/a[2]':
                 ['text()',
                 {gUrl('@href'):
                    {'.//dl/dt/a[2]':
                        ['text()',
                        {gUrl('@href'):[gContent('.//div[@class="ishop"]/table')]}
                        ]
                    }
                 }
                 ]
                 }
                 ,mydb.AnyData2MySql(mydb.InitDb('test','localhost','root',''),'metiz')
               )

    """
    if IsDocCorrect:
        local.IsDocCorrect=IsDocCorrect
    ret=ParseXDoc(UrlOrFNameOrDoc, xPaths, StoreFunc)
    if not ret:
        return []
    ret=filter(None,ret)# filter empty
    if StoreFunc:
        # make normal table form
        data=app.ArrTree2OneDimArr(ret)
        if not isinstance(StoreFunc,(tuple,list)):
            StoreFunc=[StoreFunc]
        [func(data) for func in StoreFunc]
    return ret


def IsEmpty(obj):
    if isinstance(obj,lxml.etree._Element):
        return 0
    else:
        return not obj

def ParseXDoc(UrlOrFNameOrDoc, xPaths, flNodes=0):
    #global flNoEncDec
    #flNoEncDec=1
    """
    parse doc and links in there by parameters
test=ParseAndSaveXDoc('http://www.mmk-metiz.ru/content/prices/products',
               {'.//div/dt/a[2]':
                 ['text()',
                 {gUrl('@href'):
                    {'.//dl/dt/a[2]':
                        ['text()',
                        {gUrl('@href'):[gContent('.//div[@class="ishop"]/table')]}
                        ]
                    }
                 }
                 ]
                 }
                 ,mydb.AnyData2MySql(mydb.InitDb('test','localhost','root',''),'metiz')
               )

    """
    # debug mode
#    if ParseLinksLimit<10:
#        print xPaths

    if IsEmpty(UrlOrFNameOrDoc):
        return None

#    if '\n' in xPaths:
#        xPaths=xPathsFromStrTree(xPaths)

    if isinstance(UrlOrFNameOrDoc,(tuple,list)):
        pars=map(lambda doc: [doc, xPaths, flNodes],UrlOrFNameOrDoc)
        if Threads4Parse:
            ret=threads.Threads.StartAndWait(ParseXDoc,pars,Thread_RepeatIfExcept,Threads4Parse)
            return ret.values()
        else:
            return map(lambda x: ParseXDoc(*x),pars)

    if isinstance(UrlOrFNameOrDoc,(basestring)):
#        if ''.join(map(chr,[109, 97, 114, 97, 116, 104, 111, 110, 98, 101, 116, 46, 99, 111, 109])) not in UrlOrFNameOrDoc:
#            return ''
        doc=UrlSaveGetXDoc(UrlOrFNameOrDoc)
    else:
        doc=UrlOrFNameOrDoc

    if IsEmpty(doc):
        return None

    if IsEmpty(xPaths):
        return None

    if isinstance(xPaths,(basestring)):
        if flNodes==0:
            ret=xValues(doc,xPaths,flEncode=1)
            return ret
        else:
            return xNodes(doc,xPaths)

    if op.isCallable(xPaths):
        return xPaths(doc)

    # check for dict
    if op.isMappingType(xPaths):
        pars=[[k,v] for k,v in xPaths.items()]

        if Threads4Parse:
            pars1=[[doc,k,1] for k,v in pars]
            ret=threads.Threads.StartAndWait(ParseXDoc,pars1,Thread_RepeatIfExcept,Threads4Parse)
            pars1=[[k,v, flNodes] for k,v in zip(ret.values(),[v for k,v in pars])]
            ret=threads.Threads.StartAndWait(ParseXDoc,pars1,0,Threads4Parse)
            return ret.values()
        else:
            ret=[]
            for k,v in pars:
                dPar=ParseXDoc(doc,k,1)
                ret1=ParseXDoc(dPar,v, flNodes)
                ret.append(ret1)
            return ret

    #check for list (return just values)
    if isinstance(xPaths,(tuple,list)):
        return [ParseXDoc(doc,xPath,0) for xPath in xPaths]

