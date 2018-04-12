#module to parse infromtion from htmls/xml documents
#simplified. no threads, no file downloads 
import curl,threading, StringIO
import socket,urllib,urllib2, cookielib
import collections
from collections import OrderedDict
import time
import lxml
import lxml.html
from lxml.cssselect import CSSSelector
from lxml import etree
import operator as op,os
urllib2.socket.setdefaulttimeout(30)
socket.setdefaulttimeout(60)
local=threading.local()

def cReq(CookieIdent='cookie.txt'):
    global local
    UseSsl=1
    flUseExistCurl=0
    if not getattr(local,'CookieFile',''):
    		local.CookieFile=CookieIdent

    if flUseExistCurl:
        if not hasattr(local,'fcReq'):
            ret=local.fcReq=curl.Curl()
        else:
            return local.fcReq
    else:
        ret=curl.Curl()

    ret.set_option(curl.pycurl.USERAGENT,'Mozilla/5.0 (Windows; U; Windows NT 5.2; ru; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
    ret.set_option(curl.pycurl.FOLLOWLOCATION,True)

    if local.CookieFile:
        ret.set_option(curl.pycurl.COOKIEJAR,local.CookieFile)
        ret.set_option(curl.pycurl.COOKIEFILE,local.CookieFile)

    if UseSsl:
        ret.set_option(curl.pycurl.CAINFO, 'ca-bundle.crt')
        ret.set_option(curl.pycurl.SSLCERT, 'cacert.pem')
        ret.set_option(curl.pycurl.CAPATH,'/')
        ret.set_option(curl.pycurl.SSLVERSION, 3)
        ret.set_option(curl.pycurl.SSLCERTTYPE,'PEM')
        ret.set_option(curl.pycurl.SSL_VERIFYPEER, 1)
        ret.set_option(curl.pycurl.SSL_VERIFYHOST, 2)

    ret.set_timeout(60)
    ret.set_option(curl.pycurl.CONNECTTIMEOUT, 13)
    return ret

def UrlData(url,PostParams=None):
    req=cReq()
    if isinstance(url,unicode):
        url=url.encode('utf-8')
    if PostParams:
#        print PostParams
        ret=req.post(url,PostParams)
    else:
        ret=req.get(url)
#    time.sleep(1)
    req.close()
    req=None
    return ret

def xDocFromXml(FileName):
    parser = etree.XMLParser()
    ret = etree.parse(FileName, parser)
    return ret

def xDoc(url,PostParams=None):
    if os.path.isfile(url):
        with open(url) as f:
            Data=f.read()
    else:
        Data=UrlData(url,PostParams)
    parser = etree.HTMLParser()
    return etree.parse(StringIO.StringIO(Data), parser)

def xDocFromData(data):
    parser = etree.HTMLParser()
    return etree.parse(StringIO.StringIO(data), parser)

def xNodeContent(node):
    if not hasattr(node,'itertext'):
        return unicode(node)

    l=node.itertext()
    if l is None:
        return ''

    l=list(l)
    if not l:
        return ''
    return ''.join(l)

def xNodes(Node,xPath, CheckCount=0):
    ret=Node.xpath(xPath)
    if (CheckCount>0) and (len(ret)<>CheckCount):
        raise BaseException('def xValues. Wrong matches count! CorrectCount=%s; Matches.Count=%s; XPath=%s'%(CheckCount, len(ret),xPath))
    return ret

def xNode(Node,xPath, flRaise=1):
    ret=xNodes(Node,xPath,flRaise)
    if len(ret)<>1:
        return None
    return ret[0]

def xValues(Node,xPath, CheckCount=0):
    ret=xNodes(Node,xPath, CheckCount)
    return map(lambda x:xNodeContent(x),ret)

def xValue(Node,xPath='.', flRaise=1,Default=''):
    ret=xValues(Node,xPath, flRaise)
    return (ret and ret[0]) or Default

def WebFormPost(url,PostParams={},frmFilter=None,checkForLogin=0, flJustGetActParams=0, flNoError=0):
    keys=PostParams.keys()
    frmLoginRule=' and '.join(map(lambda x: 'count(.//*[@name="%s"])>0'%x,keys))
    LoginForm='.//form[%s]'%frmLoginRule
##    udata=UrlData(url)
    d=XDoc(url)
    frms=xNodes(d,LoginForm)
    if not frms:
        if checkForLogin:
            return d
        else:
            raise BaseException('WebFormPost. Cannot find form')
    frm=filter(lambda x: not frmFilter or len(xNodes(x,frmFilter))>=1,frms)[0]
    act=xValue(frm,'@action')
    method=xValue(frm,'@method').lower().strip()
    nPars=xNodes(frm,'.//*[(@name!="")]')
    #print nPars
    r=[(xValue(n,'@name').encode('utf-8'),xValue(n,'@value',0,'').encode('utf-8')) for n in nPars ]
    r=filter(lambda x : x[0]!='',r)
    r=OrderedDict(r)
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

    doc=XDoc(act,PostParams=r)

    if checkForLogin and xNodes(doc,LoginForm):
        raise BaseException('Login Error')
    return doc

def xHtmls(Node,xPath, CheckCount=0):
    ret=xNodes(Node,xPath, CheckCount)
    ret=[lxml.html.tostring(x,pretty_print=False,encoding='utf-8') for x in ret]
    return ret

def xHtml(Node,xPath='.', flRaise=1,Default='',flEncode=1):
    ret=xHtmls(Node,xPath, flRaise)
    return (ret and ret[0]) or Default

def css(s,sAddPath=''):
    ret = CSSSelector(s)
    return ret.path+sAddPath

def IsEmpty(obj):
    if isinstance(obj,lxml.etree._Element):
        return 0
    else:
        return not obj

arrVal=lambda x : (isinstance(x,(tuple,list)) and (((len(x)==1) and arrVal(x[0])) or ((len(x)>1) and map(arrVal,x)))) or x or ''

def ParseXDoc(UrlOrFNameOrDoc, xPaths, flNodes=0):
    if IsEmpty(UrlOrFNameOrDoc):
        return None

    if isinstance(UrlOrFNameOrDoc,(tuple,list)):
        pars=map(lambda doc: [doc, xPaths, flNodes],UrlOrFNameOrDoc)
        return map(lambda x: ParseXDoc(*x),pars)

    if isinstance(UrlOrFNameOrDoc,(basestring)):
        doc=xDoc(UrlOrFNameOrDoc)
    else:
        doc=UrlOrFNameOrDoc

    if IsEmpty(doc):
        return None

    if IsEmpty(xPaths):
        return None

    if isinstance(xPaths,(basestring)):
        if flNodes==0:
            ret=xValues(doc,xPaths)
            return ret
        else:
            return xNodes(doc,xPaths)

    if op.isCallable(xPaths):
        return xPaths(doc)

    # check for dict
    if op.isMappingType(xPaths):
        pars=[[k,v] for k,v in xPaths.items()]
        ret=[]
        for k,v in pars:
            dPar=ParseXDoc(doc,k,1)
            ret1=ParseXDoc(dPar,v, flNodes)
            ret.append(ret1)
        return ret

    #check for list (return just values)
    if isinstance(xPaths,(tuple,list)):
        return [ParseXDoc(doc,xPath,0) for xPath in xPaths]

