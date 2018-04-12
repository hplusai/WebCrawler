# coding=utf-8
import os, sys, time
import app, fsys, SmartTypes,threads,web_crawler
import urllib, itertools
from sys import exit
import subprocess, re
from urlparse import urljoin, urlparse
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import random

reProxy=re.compile(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):(\d+)\b')
#p1=r'([0-9]{3}[.][0-9]{3}[.][0-9]{3}[.][0-9]{3}[:][0-9]{5})'
#p2=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#print re.findall(p,s)
#print re.findall(p1,s)
#print re.findall(p2,s)
#s=r'fdsa 210.10.20.20:123 asgfsadf'
#print reProxy.findall(s)

fProxiesThread=app.AllocLock()
SearchProxyLock=app.AllocLock()

def DefOnSearchProxy(url,proxList):
    map(AddProxy2GoodList,proxList)

OnSearchProxy=DefOnSearchProxy
#thread.allocate_lock()

Proxies=[]
CycleProxies=None
GlobalInd=0
ReuseGoodProxyTimes=1000
ReuseGoodProxyDict={}

SearchProxiesRunning=0
SearchProxiesMaxDeep=3
SearchProxiesMaxExtDeep=0
SearchProxiesMaxErrCount=0
SearchProxiesMaxUrlThreads=32

def CleanProxyList(lst):
    lst=filter(None,lst)
    return filter(None,map(lambda s:s.strip() and reProxy.findall(s) and s.strip(),lst))

ProxyBlackList=SmartTypes.UniqList(CleanProxyList(fsys.GetFileData('blacklist.txt',1)))
fsys.Save2File('blacklist.txt',ProxyBlackList)
ProxyGoodList=SmartTypes.UniqList(CleanProxyList(fsys.GetFileData('goodproxies.txt',1)))

#def RemoveFirstNum(dataProxies):
#    return map(lambda s : s.strip().split(' ')[-1].strip(),dataProxies.split('\n'))
#exit(0)

def defProcess(dataProxies):
    return CleanProxyList(dataProxies.split('\n'))

ProxiesUrls=SmartTypes.SmartDict()
ProxiesUrls['goodproxies.txt']=defProcess
#r'http://www.tubeincreaser.com/proxylist.txt':defProcess,
#r'http://multiproxy.org/txt_anon/proxy.txt':defProcess,
#r'http://multiproxy.org/txt_all/proxy.txt':defProcess,
#r'http://www.freeproxy.ru/download/lists/goodproxy.txt':RemoveFirstNum
#}

def IsUrl(Url):
    return Url and (Url[1]<>':') and (Url.startswith(r'http://') or Url.startswith(r'https://') or (re.findall(r'\.\w\w($|[\\])',Url.strip()) or '?' in Url or Url.startswith('/'))) and 1

def AddProxy2BlackList(proxy):
    global ProxyBlackList,ProxyGoodList,ReuseGoodProxyDict
    if not proxy or proxy.strip()=='':
        return

    with fProxiesThread:
        try:
            if proxy in ProxyGoodList:
                ProxyGoodList.remove(proxy)
                ReuseGoodProxyDict.pop(proxy,'nothing')
                fsys.Save2File('goodproxies.txt',ProxyGoodList)
            if proxy not in ProxyBlackList:
                ProxyBlackList.append(proxy)
#        app.Log(str(ProxyBlackList),'MATVASHU.txt')
            app.Log(proxy.strip(),'blacklist.txt',flAddTime=0)
#            fsys.Save2File('blacklist1.txt',ProxyBlackList)
        except:
            app.LogError(1)

def AddProxy2GoodList(proxy):
    global ProxyGoodList
    with fProxiesThread:
        try:
            if proxy:
                if proxy not in ProxyGoodList:
                    ProxyGoodList.append(proxy)
                UsedTimes,InUse=ReuseGoodProxyDict.get(proxy,[0,0])
                UsedTimes+=1
                if UsedTimes>=ReuseGoodProxyTimes:
                    ReuseGoodProxyDict.pop(proxy,'')
                else:
                    ReuseGoodProxyDict[proxy]=[UsedTimes,0]
    #        app.Log(str(ProxyBlackList),'MATVASHU.txt')
            fsys.Save2File('goodproxies.txt',ProxyGoodList)
        except:
            app.LogError(1)

def AddProxiesList(FileName, funcForProcessing=defProcess):
    global ProxiesUrls
    with fProxiesThread:
        ProxiesUrls[FileName]=funcForProcessing

def RefreshProxies():
    global ProxiesUrls, CycleProxies, Proxies
    Proxies=[]
    for k,v in ProxiesUrls.items():
        #print k
        try:
            if IsUrl(k):
                d=urllib.urlopen(k).read()
            else:
                d=fsys.GetFileData(k)

            Proxies+=(v and v(d)) or CleanProxyList(d.split('\n'))
        except:
            app.LogError()

    Proxies=SmartTypes.UniqList(Proxies)
#    fsys.Save2File('allproxies.txt',Proxies)
    # add dummy proxy
    if not Proxies:
        Proxies.append('0.0.0.0:80')
    CycleProxies=itertools.cycle(Proxies)
    return Proxies

def GetProxy():
    global GlobalInd, ProxyBlackList, ReuseGoodProxyDict
    with fProxiesThread:
        if ReuseGoodProxyTimes:
            lReuse=filter(lambda x : x[1][1]==0,ReuseGoodProxyDict.items())
            if lReuse:
                UsedTimes,InUse=lReuse[0][1]
                ReuseGoodProxyDict[lReuse[0][0]]=[UsedTimes,1]
                return lReuse[0][0]

        if not CycleProxies or GlobalInd>(len(Proxies)*5):
            RefreshProxies()
            GlobalInd=0

        GlobalInd+=1

        ind=0
        ret=CycleProxies.next()
        while ret in ProxyBlackList and ind<len(Proxies):
            ret=CycleProxies.next()
            ind+=1

        if ind>=len(Proxies):
            # if there is not proxies let's wait for 1 minute
            GlobalInd=0
            RefreshProxies()
#            StartSearchProxies()
            # clean black proxies list
            try:
                ProxyBlackList=[]
                os.remove('blacklist.txt')
            except:
                pass
#            time.sleep(60)
            ret=CycleProxies.next()
            #raise Exception('Cannot allocate proxy!')

        return ret

def GetHtmlLinks(url, data, flOnlyCurWebSite=1):
    soup = BeautifulSoup(data)
    ret=[str(tag['href']) for tag in soup.findAll('a', href=True)]
    pureRet=[]
    WebSite=web_crawler.GetUrlWebSite(url).strip('http://').strip('/').strip(':')
    for x in SmartTypes.UniqList(ret):
        xWebSite=web_crawler.GetUrlWebSite(x).strip('http://').strip('/').strip(':')
        nUrl=(not flOnlyCurWebSite or WebSite in x or xWebSite=='' or '') and IsProxyUrl(x)
        if nUrl:
            pureRet.append(web_crawler.DoNormUrl(nUrl))

    return SmartTypes.UniqList(pureRet)

ProxiesUrls=SmartTypes.SmartDict()

def IsProxyUrl(url):
    flNotProxyUrl=not url or not url.strip().strip('/') or 'javascript' in url or url.startswith('#') or url.endswith('.js') or url.endswith('.css') or 'google.com' in url
    return (not flNotProxyUrl) and url.strip()

def CheckProxies(pLst, NoThreads=1):
    ret=[]
    if NoThreads:
        for p in pLst:
            try:
#                d=web_crawler.GetUrlData('http://ya.ru',p)
#                if 'http://yandex.ru/opensearch.xml' in d:
                d=web_crawler.GetUrlData('http://market.yandex.ru',p)
                if '</html>' in d and 'search-input' in d:
                    ret.append(p)
            except:
                pass
    return ret

def ProcessProxyUrl(url, parent_site='', deep=0, deep_external=0):
    global ProxiesUrls
    # Do not use proxies for search
    web_crawler.local.ProxyFunc=None
    try:
        if not IsProxyUrl(url):
            return None

        # fix some bad links
        url=url.split('\\')[-1]
        url=url.strip()

        if deep_external>SearchProxiesMaxExtDeep or deep>SearchProxiesMaxDeep:
            return None

        url=urljoin(parent_site, url)

        if not IsProxyUrl(url):
            return None

        UrlWebSite=web_crawler.GetUrlWebSite(url)
        if url.strip('/')==UrlWebSite.strip('/'):
            return None

        with SearchProxyLock:
            if url in ProxiesUrls:
                return None

            ProxiesUrls[url]=''

        if not parent_site:
            parent_site=UrlWebSite
            deep+=1
        else:
            if UrlWebSite==parent_site:
                deep+=1
            else:
                deep_external+=1

        content=web_crawler.GetUrlData(url)

        try:
            lstUrls=GetHtmlLinks(url, content)
            proxList=map(lambda p : p and ('.'.join(p[:4])+':'+p[4]) ,reProxy.findall(content))
        except:
            app.LogError(flRaise=1)

        proxList=CheckProxies(proxList)
        if proxList:
#            app.Log('Before join','global.log')
#            app.Log('After join'+pd,'global.log')
            OnSearchProxy(url,proxList)

        if not lstUrls:
            return None
        params=map(lambda x : [x,parent_site,deep,deep_external],lstUrls)
        threads.Threads.StartAndWait(ProcessProxyUrl,params,SearchProxiesMaxErrCount,SearchProxiesMaxUrlThreads,flNoResult=1)
        return None
    except:
        app.LogError(url,1,'error.log')

def StartSearchProxies():
    global SearchProxiesRunning
    if SearchProxiesRunning:
        return

    with SearchProxyLock:
        SearchProxiesRunning=1

    lst=fsys.GetFileData(r'proxy_sites.txt',1)
    #do random list inplace
    random.shuffle(lst)
    threads.Threads.StartAndWait(ProcessProxyUrl,filter(lambda s : s and s.strip(),lst),SearchProxiesMaxErrCount,SearchProxiesMaxUrlThreads,flNoResult=1)

#def CheckProxiesConnectivity():
#    threads.Threads.StartAndWait('http://google.com',filter(lambda s : s and s.strip(),lst),SearchProxiesMaxErrCount,SearchProxiesMaxUrlThreads,flNoResult=1)
