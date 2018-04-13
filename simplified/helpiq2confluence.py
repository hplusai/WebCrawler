import operator as op,os, re, sys
import collections as coll
import webutils
from webutils import *

import xmlrpclib
from xmlrpclib import Server

user = sys.argv[1]
password = sys.argv[2]
server = sys.argv[3]
Space=sys.argv[4]
SrcServ=sys.argv[5]
ImpPath=sys.argv[6].split(',')

sp = Server(server)
token = sp.confluence2.login(user, password)

def confluenceFormatHtml(d,spaceKey,ps):
    global psAll
    for xn in d.xpath('.//input'):
        par=xn.getparent()
        par.remove(xn)

    for xn in d.xpath('.//img'):
        ip=xn.get('src')
        if SrcServ in ip:
            pass
        if (ip.startswith('http://') and not ip.startswith(SrcServ)) or ip.startswith('data:'):
            continue
        ip='//'+ip
        try:
            ind=ip.rindex('/images/')
            ind+=8
        except:
            pass
        xn.set('src','/images/upload/%s'%spaceKey+ip[ind:])

    for an in d.xpath('.//a[@hqid or @href]'):
        href=an.get('href')
        if href and (SrcServ in href):
            href=href.replace(SrcServ,'/')
        hqid=an.get('hqid')
        if (hqid is not None and (hqid!='')):
            href=''
            lnk=''
            lnk=xValue(an)
            if hqid in ps:
                lnk=psAll[hqid][2]
                if '/' in lnk:
                    npd=sp.confluence2.getPage(token, spaceKey, lnk)
                    href='/pages/viewpage.action?pageId=%s'%npd['id']
            else:
                pass
        else:
            pass
        if href=='':
            href='/display/%s/%s'%(spaceKey,lnk.replace(' ','+'))
        try:
            an.set('href',href)
        except:
            pass

    sHtml=xHtml(d)
    sHtml=sHtml.replace('\xa0','')
    sHtml=sHtml.replace('\xc2','&nbsp;')
    sHtml=sHtml.replace('\xab','')
    sHtml=sHtml.replace('\n','&nbsp;')
    return sHtml

def addPage(space,title,content,parent=None, parentId = None):
    npd = {"title":title,"content":content,"space":space}
    try:
        npd=sp.confluence2.getPage(token, space, title)
        npd['content']=content
    except:
        pass

    if parent:
        try:
            page = sp.confluence2.getPage(token, space, parent)
            npd['parentId']=page["id"]
        except:
            pass

    np = sp.confluence2.storePage(token, npd)
    return np

psAll={}
def HelpIq2Confluence(mainPath):
    global psAll,Space
    spaceKey=Space
#    mainPath=r'G:\Work\HelpIQ2Confluence\Info\2'
    with open(mainPath+r'\help.xml','rb') as f:
        xmlData=f.read()
#    fsys.GetFileData()
    xmlData=xmlData.replace('&','')
    xd=lxml.etree.XML(xmlData)

    ors=ParseXDoc(xd,{'.//order':['node_id', 'node_order', 'parent_id']})
    ors=arrVal(ors)
    for i in xrange(len(ors)):
        nId,nO,nP=ors[i]
        ors[i]=[nId.split(';')[-1],nO,nP.split(';')[-1]]

    ps=ParseXDoc(xd,{'.//page':['topic_id', 'topic_type', 'topic_title','folder_id','file_name']})
    ps=arrVal(ps)
    ps=dict([[x[0],x] for x in ps])

    oKeys=[x[0] for x in ors]

    fls=ParseXDoc(xd,{'.//folder':['folder_id','parent_id','folder_name']})
    fls=arrVal(fls)
    for fId,pId,fN in fls:
        ps[fId]=[fId,'Folder',fN,fId,None]
        if fId not in oKeys:
            ors.append([fId,'9999',pId])

#    for k,v in ps.items():
#        v[2]=v[0]+'.'+v[2]
    ors.sort(key=lambda x:(int(x[2]),int(x[1])))
    lastO=0
    for i in xrange(len(ors)):
        nId,nO,nPid=ors[i]
        cur=ps[nId]
        if nO=='9999':
            lastO+=1
            nO=str(lastO)
            ors[i][1]=nO
        else:
            lastO=int(nO)
        cur[2]=nO+'.'+cur[2]

    psAll.update(ps)
    for nId,nO,nPid in ors:
        cur=ps[nId]
        tId,tType,tT,fId,fN=cur
        fd=' '
        if fN:
            fd=xDoc(mainPath+'\\'+fN)
            n=xNode(fd,'.//body')
#            fd=xHtml(n)
            fd=confluenceFormatHtml(n,spaceKey,ps)
        par=None
        nPid=nPid.split(';')[-1]
        if int(nPid)>0:
            if (nPid in ps):
                par=ps[nPid][2]
            else:
                pass

        fd='<ac:structured-macro ac:name="html"><ac:plain-text-body><![CDATA['+fd+']]></ac:plain-text-body></ac:structured-macro>'
        try:
            np=addPage(spaceKey,tT,fd,par)
        except:
            raise
            pass


map(HelpIq2Confluence,ImpPath)