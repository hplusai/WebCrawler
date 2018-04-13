# coding=utf-8
import tempfile,sys
import utils
from utils import web, proxies
from utils.web import *
import operator as op,os, re
#import certifi
#import spynner
#import mechanize
#from mechanize import HTTPRedirectHandler,HTTPEquivProcessor,HTTPRefreshProcessor,HTTPRefererProcessor#HTTPCookieProcessor,
import threading,traceback
import uuid
import time, random, subprocess
import imghdr

def DocCheck(s):
    sl=str(s).lower()
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

GlobalDocCorrect=getattr(app.params,'DocCheck',DocCheck)
AdditionalDocCheck=getattr(app.params,'AdditionalDocCheck',None)
onFormatCacheUrl=getattr(app.params,'onFormatCacheUrl',StdCacheUrl)

EnableCache=getattr(app.params,'EnableCache',1)
OnlyCache=getattr(app.params,'OnlyCache',0)
flRebuildCache=getattr(app.params,'RebuildCache',1)

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

def css(s,sAddPath=''):
    ret = CSSSelector(s)
    return ret.path+sAddPath

def WebFormPost(url,PostParams={},frmFilter=None,checkForLogin=0, flJustGetActParams=0, flNoError=0):
    if isinstance(url,(str,)):
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
    frm=list(filter(lambda x: not frmFilter or len(xNodes(x,frmFilter))>=1,frms))[0]
    act=xValue(frm,'@action')
    method=xValue(frm,'@method').lower().strip()
    r=ParseXDoc(frm,{'.//*[@name!=""]':['@name','@value']})
    r=app.ArrTree2OneDimArr(r)
    r=list(filter(lambda x : x[0]!='',r))
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

flUseExistCurl=False
CookieFile=None#app.AbsPath('curl.cookies')
cookiesLocation='cookies'
if not os.path.exists(app.AbsPath(cookiesLocation)):
    os.mkdir(app.AbsPath(cookiesLocation))

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
                    if not isinstance(h, str):
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
                return RequestData(sUrl,pPostParams,pProxy)
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
            	hash = app.md5(urlCache).hexdigest()
            cacheFile=cacheLocation + "/" + hash + ".html"
            if os.path.exists(cacheFile) and not flRebuildCache:# and not postParams:
                ret=fsys.GetFileData(cacheFile,0,'rb')
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
                if cacheFile!='':
                    try:
                        os.remove(cacheFile)
                    except:
                        pass
                raise Exception('IsDocCorrect Failed :Url= %s \n %s'%(url,ret))

        if 'Bad Request' in str(ret) and len(ret)<500:
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

def GetXDoc(Url,Proxy=None, postParams=None):
    app.Log('GetXDoc('+Url+')')
    if proxies.IsUrl(Url):
        Data=GetUrlData(Url, Proxy, postParams)
    else:
        Data=fsys.GetFileData(Url)
        enc=GetCharset(Data,None)
        if enc:
            Data=fsys.GetFileData(Url,Encoding=enc)

    if not Data or Data.strip()=='':
        app.Log('Exception : NO DATA in GetXDoc','ERROR.log')
        return None

    return GetXDocFromData(Data)

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
    ret=list(filter(None,ret))# filter empty
    if StoreFunc:
        # make normal table form
        data=app.ArrTree2OneDimArr(ret)
        if not isinstance(StoreFunc,(tuple,list)):
            StoreFunc=[StoreFunc]
        [func(data) for func in StoreFunc]
    return ret

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
        pars=list(map(lambda doc: [doc, xPaths, flNodes],UrlOrFNameOrDoc))
        if Threads4Parse:
            ret=threads.Threads.StartAndWait(ParseXDoc,pars,Thread_RepeatIfExcept,Threads4Parse)
            return ret.values()
        else:
            return list(map(lambda x: ParseXDoc(*x),pars))

    if isinstance(UrlOrFNameOrDoc,(str,)):
#        if ''.join(map(chr,[109, 97, 114, 97, 116, 104, 111, 110, 98, 101, 116, 46, 99, 111, 109])) not in UrlOrFNameOrDoc:
#            return ''
        doc=UrlSaveGetXDoc(UrlOrFNameOrDoc)
    else:
        doc=UrlOrFNameOrDoc

    if IsEmpty(doc):
        return None

    if IsEmpty(xPaths):
        return None

    if isinstance(xPaths,(str,)):
        if flNodes==0:
            ret=xValues(doc,xPaths,flEncode=1)
            return ret
        else:
            return xNodes(doc,xPaths)

    if hasattr(xPaths, "__call__"):
        return xPaths(doc)

    # check for dict
    if is_dict(xPaths):
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

