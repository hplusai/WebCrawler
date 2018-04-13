# coding=utf-8
import socket,urllib,re, os
try:
#py2
  import httplib
  import HTMLParser
  import cookielib
  import urllib2
  import urlparse
  from urlparse import urljoin, urlsplit, parse_qs, urlparse
  from StringIO import StringIO
except:
#p3
  import urllib.request as urllib2
  from urllib.parse import urljoin, urlsplit, parse_qs, urlparse
  from io import StringIO
  import http.client as httplib
  import html.parser as HTMLParser
  import http.cookiejar as cookielib

import lxml
import lxml.html
from lxml.cssselect import CSSSelector
from lxml import etree
import requests
import utils
from utils import app, fsys, SmartTypes,threads
from utils.app import local, is_dict

import chardet

urllib2.socket.setdefaulttimeout(30)
socket.setdefaulttimeout(60)

redirect_re = re.compile('<meta[^>]*?url=(.*?)["\']', re.IGNORECASE)

#DefEnc='utf-8'
#DetectedEncoding=None
flNoEncDec=1

CurlTimeOut=getattr(app.params,'TimeOut',13)
CurlConnectTimeOut=getattr(app.params,'ConnectTimeOut',5)
MsWordLock=app.AllocLock()
AutoFixLinks=getattr(app.params,'AutoFixLinks',1)

WebSiteEncoding=app.UnpickleObj('web_enc.obj') or {}

reProxy=re.compile(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):(\d+)\b')
#p1=r'([0-9]{3}[.][0-9]{3}[.][0-9]{3}[.][0-9]{3}[:][0-9]{5})'
#p2=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#print re.findall(p,s)
#print re.findall(p1,s)
#print re.findall(p2,s)
#s=r'fdsa 210.10.20.20:123 asgfsadf'
#print reProxy.findall(s)

def GetCharset(data,defenc='utf-8'):
    ret=re.findall("""<meta.*?charset=([^"']+)""",data,re.IGNORECASE)
    if not ret:
        ret=re.findall("""encoding=([^"']+)""",data,re.IGNORECASE)
    if not ret:
        return defenc
    return ret[0]

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

def GetUrlWebSite(Url):
    parsed_uri = urlparse(Url)
    domain = '{}://{}/'.format(parsed_uri[0], parsed_uri[1])
    return domain

def IsUrl(Url):
    return Url and (Url[1]!=':') and (Url.startswith(r'http://') or Url.startswith(r'https://') or (re.findall(r'\.\w\w($|[\\])',Url.strip()) or '?' in Url or Url.startswith('/'))) and 1

def GetUrlDataAndLinks(url, flOnlyCurWebSite=1):
    doc=GetXDocFromData(data)
    ret=xValues(doc,'.//a/@href')
    #ret=[str(tag['href']) for tag in soup.findAll('a', href=True)]
    pureRet=[]
    WebSite=web.GetUrlWebSite(url).strip('http://').strip('/').strip(':')
    for x in SmartTypes.UniqList(ret):
        xWebSite=web_crawler.GetUrlWebSite(x).strip('http://').strip('/').strip(':')
        nUrl=(not flOnlyCurWebSite or WebSite in x or xWebSite=='' or '') and IsProxyUrl(x)
        if nUrl:
            pureRet.append(web_crawler.DoNormUrl(nUrl))

    return SmartTypes.UniqList(pureRet)

def IsProxyUrl(url):
    flNotProxyUrl=not url or not url.strip().strip('/') or 'javascript' in url or url.startswith('#') or url.endswith('.js') or url.endswith('.css') or 'google.com' in url
    return (not flNotProxyUrl) and url.strip()

def BasicAuthAndGetPages(rooturl='http://192.168.1.1',username='admin',password='admin',urls=[]):
    # set root url
    DoNormUrl(rooturl)
    # create a urllib2 opener for basic authentication
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, rooturl, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    return list(map(lambda url : urllib2.urlopen(DoNormUrl(url)).read(),urls))

def RequestData(url,pPostParams=None,proxy=None):
    local.sHostName=url
    if getattr(local,'cj',None) is None:
        local.cj = cookielib.MozillaCookieJar(local.CookieFile)
        if not proxy and os.access(local.CookieFile, os.F_OK):
            local.cj.load(ignore_discard=True)

    r = requests.request(url=url,headers={'User-agent': 'Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.8.131 Version/11.10'},method=(pPostParams and 'POST') or 'GET',params=pPostParams,cookies=local.cj,timeout=CurlTimeOut,allow_redirects=True,proxies=(proxy and {'http': proxy}) or None, verify=True)#,'https':pProxy,'ftp':pProxy
    return r.content

def FixLinks(d):
    n=xNodes(d,'.//a')
    for x in n:
        href=x.attrib.get('href','').strip()
        if (href!='') and (href!='#') and not href.lower().startswith('javascript:'):
            np=urljoin(local.sHostName,href)
            try:
                x.attrib['href']=np
            except:
                print('FixLinks error : ',np)

def GetXDocFromData(Data,Encoding=None):
    #auto detect and remove xmlns
    #<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" # lang="ru">
    Data=str(Data)
    if 'xmlns=' in Data:
        Data=Data.replace('xmlns=','this_xmlns_was_removed_case_libxml2=')

    Encoding=Encoding or GetCharset(Data) #GetWebSiteEncoding(None,Data)

    try:
        #ret=libxml2.htmlParseDoc(Data,Encoding)
        parser = etree.HTMLParser()
        #(isinstance(Data,unicode) and Data) or Data.decode(Encoding))
        #or ' charset="utf' in Data
#        if (not isinstance(Data,str)):
#            enc=GetCharset(Data)
#            Data=Data.decode(enc)
        ret = etree.parse(StringIO(Data), parser)

        if AutoFixLinks:
            FixLinks(ret)
    except:
        app.LogError(Data,1,'libxml_error.log')

    return ret

def GetXDocFromXml(FileName):
    parser = etree.XMLParser()
    ret = etree.parse(FileName, parser)
    return ret

def GetXDocFromWord(Url):
    from win32com.client import DispatchWithEvents, Dispatch
    Data=GetUrlData(urllib2.unquote(Url))
    docName=fsys.GetTempFilename('.doc');
    fsys.Save2File(docName,Data,'wb')
    # only one Ms word document (no multithreads)
    MsWordLock.acquire()
    try:
        import pythoncom
        pythoncom.CoInitialize()
        word = Dispatch("Word.Application")
        word.Visible=1
        doc=word.Documents.Open(docName,Revert=1,Visible=0,OpenAndRepair=1)
        htmName=fsys.GetTempFilename('.htm');
        word.ActiveDocument.SaveAs(htmName,8);
        doc.Close()
    finally:
        MsWordLock.release()
    return GetXDoc(htmName)

def Div(Html,Class=''):
    return '<div class="%s">'%Class+Html+'</div>'

def SmartXpath(Node,xPath):
#    DecXPath=DecRus(xPath.replace('->','following-sibling::node()[1]').replace('<-','preceding-sibling::node()[1]'))
    DecXPath=xPath.replace('->','following-sibling::node()[1]').replace('<-','preceding-sibling::node()[1]')
    try:
#      return Node.xpath(DecRus(DecXPath))
      return Node.xpath(DecXPath)
    except:
        app.LogError('SmartXpath.'+DecXPath,1)

def xNodes(Node,xPath, CheckCount=0):
    ret=SmartXpath(Node,xPath)
    if (CheckCount>0) and (len(ret)!=CheckCount):
        err='CorrectCount=%s;\nMatches.Count=%s;\nXPath=%s;\nurl=%s'%(CheckCount, len(ret),xPath,GetDocUrl(Node))
        app.Log(err,'Wrong_matches_count.log')
        if NoErrorsMode:
            ret=[None]*CheckCount
        else:
            raise BaseException(err)
    return ret

def xNode(Node,xPath, flRaise=1):
    ret=xNodes(Node,xPath,flRaise)
    if len(ret)!=1:
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
    return list(map(xNodeContent,ret))#map(lambda x:(flEncode and EncRus(xNodeContent(x))) or xNodeContent(x),ret)
    
def xValue(Node,xPath='.', flRaise=1,Default='',flEncode=1):
    ret=xValues(Node,xPath, flRaise, flEncode)
    return (ret and ret[0]) or Default

#def xProps(Node):
#    return SmartDict([[x.name,xNodeContent(x)] for x in Node.properties if x.type=='attribute'])

def xHtmls(Node,xPath, CheckCount=0,flEncode=1,subPathes=[]):
    ret=xNodes(Node,xPath, CheckCount)
    ret=[((x is not None) and lxml.html.tostring(x,pretty_print=True,encoding='utf-8',with_tail=False)) or '' for x in ret]
    return ret#map(lambda x:(flEncode and EncRus(x)) or x,ret)

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
    def __init__(_,xpathOrFunc, flRaiseIfNotFound=1):
        _.xpathOrFunc=xpathOrFunc
        _.flRaiseIfNotFound=flRaiseIfNotFound

    def __call__(_,doc):
        xp=app.CallOrReturn(_.xpathOrFunc)
        r=xValues(doc,xp)

        # raise error
        if not r and _.flRaiseIfNotFound:
            return xValue(doc,xp,1)

        return [UrlSaveGetXDoc(v,doc) for v in r]

class gContent():
    """Evaluate Xpath or function for current doc,and return serialized value for node
IMPORTANT!!! First function param Document."""
    def __init__(_,xpathOrFunc,enc='utf8'):
        _.xpathOrFunc=xpathOrFunc
        _.enc=enc

    def __call__(_,doc):
        node=xNode(doc,app.CallOrReturn(_.xpathOrFunc))
        return lxml.html.tostring(node,pretty_print=True)

class gConst():
    """just return const value
"""
    def __init__(_,val):
        _.val=val

    def __call__(_,doc):
        return _.val

def gFileAutoNaming(doc,iUrl):
    tmpDir=app.AbsPath('temp')
    fsys.CreateDirs(tmpDir)
    return fsys.GetTempFilename(dir=tmpDir)

class gFile():
    """Evaluate Xpath or function for current doc and return list of filenames saved to disk
Also you can use custom defined function for filenames,
in other case temp filenames
IMPORTANT!!! First function param Document."""
    def __init__(_,xpathOrFunc,fname=gFileAutoNaming):
        _.xpathOrFunc=xpathOrFunc
        _.fname=fname
#        _.enc=enc

    def __call__(_,doc):
        if callable(_.xpathOrFunc):
            iUrl=_.xpathOrFunc(doc)
        else:
            iUrl=xValue(doc,_.xpathOrFunc)
        fname=app.CallOrReturn(_.fname,doc,iUrl)
        if not(EnableCache and os.path.exists(fname)):
            fsys.Save2File(fname,GetUrlData(iUrl),'wb')
        return fname

def GetDocUrl(CurDoc):
    return ((not IsEmpty(CurDoc)) and ((hasattr(CurDoc,'getroottree') and CurDoc.getroottree()) or CurDoc).getroot().get('docurl')) or ''

def IsEmpty(obj):
    if isinstance(obj,lxml.etree._Element):
        return 0
    else:
        return not obj

#--bugfix
def FreeAndNil(doc):
    try:
        doc.free()
        doc=None
    except:
        pass

def DetectFileEnc(fName, DefEncRes='utf-8'):
    cd=chardet.detect(fsys.GetFileData(fName))
    return (cd and cd['encoding']) or DefEncRes
