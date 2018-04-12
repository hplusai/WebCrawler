# -*- coding: cp1251 -*-
import utils
from utils import fileutils, SmartTypes, apputils#, HtmlHelper
from apputils import AbsPath
from HtmlHelper import xNodes,xValues,GetXDocFromXml
import itertools
from itertools import chain
import distutils
import libxml2
import chardet,re

def DoubleQuotas(s):
    return '"%s"'%s

def Arr2Line(arr,sep=';',addfun=None):
    ret=''
    if not arr:
        return ret
    for x in arr:
        if addfun:
            x=addfun(x)
        ret+=x+sep
    
    return ret[:-1]

def ToUtf(s):
    return s.decode('cp1251').encode('utf8')

def NormStr(s):
    return s.replace('\r\n','^').replace('\r','^').replace('\n','^')

def DeNormStr(s):
    return s.replace('^','\n')

def CollectWordsFromTextFiles(Path):
    ret={}
    fl=distutils.filelist.findall(Path)
    for fName in fl:
        text=fileutils.GetFileData(fName,Encoding='utf16')
        # replace new line symbols
        text=NormStr(text.strip())
        if isEnglish(text):
            ret[text]='swf'
    # check encoding
    
#    alldata=reduce(lambda ret,x: ret+' '+x,ret.keys())
#    print chardet.detect(alldata)
    return ret

creXPathPos=re.compile('\[\d+\]')

def RemoveXPathPositions(XPath):
    return reduce(lambda ret,x : ret.replace(x,''),creXPathPos.findall(XPath),XPath)

def getTextNode(xnode):
    if not xnode.children:
        return None
    for x in xnode.children:
        if x.name=='text':
            return x
    return None

def AnalyzeXmlFiles(Path):
    global xN
    ret={}
    fl=distutils.filelist.findall(Path)
    for fName in fl:
        print fName
        d=GetXDocFromXml(AbsPath(fName))
        #Nodes+#Attributes
        for xN in (xNodes(d,'.//*')+xNodes(d,'.//@*')):
            try:
                if isinstance(xN,libxml2.xmlAttr):
#                    print xN.nodePath()
                    tNode=xN
                else:
                    tNode=getTextNode(xN)
                    
                if tNode and tNode.content.strip() and isEnglish(tNode.content):
                    xpath=RemoveXPathPositions(xN.nodePath())
                    cont=NormStr(tNode.content)
                    if not (xpath in ret):
                        ret[xpath]={}
                    ret[xpath][cont]=None
            except:
                print 'Error',xN.nodePath()
                break
#        break
    return ret

#ax=AnalyzeXmlFiles(r'G:\Data')

def CollectWordsFromXmlFiles(Path,XmlXPathList):
    global xN
    ret={}
    fl=distutils.filelist.findall(Path)
    for fName in fl:
#        print fName
        d=GetXDocFromXml(AbsPath(fName))
        for xN in (xNodes(d,'.//*')+xNodes(d,'.//@*')):
            try:
                if isinstance(xN,libxml2.xmlAttr):
                    tNode=xN
                else:
                    tNode=getTextNode(xN)
                    
                if tNode and tNode.content.strip() and isEnglish(tNode.content):
                    xpath=RemoveXPathPositions(xN.nodePath())
                    if not (xpath in XmlXPathList):
                        continue
                    
                    cont=NormStr(tNode.content.strip())
                    ret[cont]=xpath
            except:
                print 'Error',xN.nodePath()
                break
#        break
    return ret

def GetTranslateDict(FileName=None):
    tDict={}
    dData=fileutils.GetFileData(FileName or AbsPath(r'translate.csv'),1)
    for x in dData:
        u=x.split(';')
        if len(u)==1:
            tDict[u[0]]=''
        else:
            tDict[u[0]]=DeNormStr(u[1].strip())
    return tDict

def UpdateWordsInMainXml():
    # init dict
    fName=AbsPath(r'main_movie.xml')
    xDoc=libxml2.parseFile(fName)
    tDict=GetTranslateDict()
    for xN in xDoc.xpathEval('.//DefineEditText'):
        tId=xN.prop("ID")
        fontId=xN.prop("FontID")
        fHeight=xN.prop("Height")
        fColor=xN.prop("Color")
        fAlign=xN.xpathEval('./Layout/@Align')
        fAlign=(fAlign and fAlign[0].content) or ''

        #tEng=NormStr(tOrigText[tId])
#        if isEnglish(tEng):
        fTextNode=xN.xpathEval('./Value')
        if not fTextNode:
            continue
        fTextNode=fTextNode[0].children
        xN.setProp('UseOutlines','False')
            # search CDATA child
        while fTextNode.type!='cdata':
            fTextNode=fTextNode.next
        if not fTextNode:
            raise xN.content
        tEng=NormStr(fTextNode.content)
        s=tEng
        print 'UpdateWordsInMainXml Trying ID=%s'%tId
        if tEng.startswith('<p '):
            try:
              doc=libxml2.parseDoc(s)
              s=NormStr(doc.content)
            except:
                pass
        s=s.strip()
        if not isEnglish(s):
            continue
        if s in tDict:
            fText=tDict[s]
#           fText=GetHtmlText(tId,fontId,ToUtf(DeNormStr(fText)),fHeight,fColor,fAlign)
            fTextNode.setContent(ToUtf(DeNormStr(tEng.replace(s,fText))))
        else:
            print 'Do not find ID=%s, Text="%s" '%(tId,s)

##        xN.setProp('AutoSize','True') - IT IS CRASH THE GAME
#        xN.setProp('HTML','True')
    xDoc.saveFile(fName)

def UpdateWordsInXmlFiles(Path,XmlXPathList):
    global xN
#    ret={}
    fl=distutils.filelist.findall(Path)

    # init dict
    tDict=GetTranslateDict()
    
    for fName in fl:
        d=GetXDocFromXml(AbsPath(fName))
        for xN in (xNodes(d,'.//*')+xNodes(d,'.//@*')):
            try:
                if isinstance(xN,libxml2.xmlAttr):
                    tNode=xN
                else:
                    tNode=getTextNode(xN)
                    
                if tNode and tNode.content.strip() and isEnglish(tNode.content):
                    xpath=RemoveXPathPositions(xN.nodePath())
                    if not (xpath in XmlXPathList):
                        continue
                    cont=NormStr(tNode.content.strip())
                    
                    if tDict.has_key(cont):
                        xN.setContent(ToUtf(tDict[cont]))
                    else:
                        print 'not found %s; xpath=%s'%(cont,xpath)
#            k=val.decode('cp1251')
#                    ret[cont]=xpath
            except:
                print 'Error',xN.nodePath()
                break
        d.saveFileEnc(AbsPath(fName),'utf-8')
#        break
#    return ret


#print CollectWordsFromXmlFiles(r'G:\Data',XmlXpathList)

##for k,v in ax.items():
##... 	vk=v.keys()
##... 	if vk and not any(map(lambda x: vk[0].find(x)>=0,['.mp3','.swf','.jpg','.xml'])):
##... 		print k,v.keys()[:3]
