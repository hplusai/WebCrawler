# coding=utf-8
from __future__ import print_function
import os
import re
import traceback
import sys, re, datetime
import time,thread, threading
import fileutils
#import pickle
import cPickle as pickle
import inspect
import sets
import operator as op
import Queue
import uuid, md5
#import SmartTypes
import locale
import SmartTypes
import shlex, subprocess
import chardet
import socket,select
import communication
locale.setlocale(locale.LC_ALL,'Russian')

#exit(0)

local=threading.local()

#flAlwaysUnicode=false

#z=thread.allocate_lock()
#z.acquire_lock(blocking=True, timeout=20)
#z=thread.allocate_lock(1,10)
#print 'tested'
#exit(0)

def uid():
    uuid

##uniqId=0
##def unique_id():
##    global uniqId
##    while 1:
##        yield uniqId
##        uniqId+=1
##
##uniqgen=unique_id()
import time

class singleinstance:
    """ Limits application to single instance """
    def __init__(self):
        from win32event import CreateMutex
        from win32api import GetLastError

        self.mutexname = "testmutex_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
        self.mutex = CreateMutex(None, False, self.mutexname)
        self.lasterror = GetLastError()

    def aleradyrunning(self):
        from winerror import ERROR_ALREADY_EXISTS
        return (self.lasterror !=0) #== ERROR_ALREADY_EXISTS)

    def __del__(self):
        from win32api import CloseHandle
        if self.mutex:
            CloseHandle(self.mutex)

'''
class SafeLock(object):
    def __init__(self, key, expires=60, timeout=10):
        """
        Distributed locking using Redis SETNX and GETSET.

        Usage::

            with Lock('my_lock'):
                print "Critical section"

        :param  expires     We consider any existing lock older than
                            ``expires`` seconds to be invalid in order to
                            detect crashed clients. This value must be higher
                            than it takes the critical section to execute.
        :param  timeout     If another client has already obtained the lock,
                            sleep for a maximum of ``timeout`` seconds before
                            giving up. A value of 0 means we never wait.
        """

        self.key = key
        self.timeout = timeout
        self.expires = expires

    def __enter__(self):
        timeout = self.timeout
        while timeout >= 0:
            expires = time.time() + self.expires + 1

            if redis.setnx(self.key, expires):
                # We gained the lock; enter critical section
                return

            current_value = redis.get(self.key)

            # We found an expired lock and nobody raced us to replacing it
            if current_value and float(current_value) < time.time() and \
                redis.getset(self.key, expires) == current_value:
                    return

            timeout -= 1
            time.sleep(1)

        raise LockTimeout("Timeout whilst waiting for lock")

    def __exit__(self, exc_type, exc_value, traceback):
        redis.delete(self.key)
'''
class LockTimeout(BaseException):
    pass

#s12='''
class SafeLock(object):
    def __init__(self):
        self._lock = threading.Lock()
    def acquire(self):
#        print "acquired", self
        #traceback.print_tb
        i=0
        while i<100:
            if self._lock.acquire(False):
                return
            time.sleep(0.01)

        raise LockTimeout(traceback.format_stack())
#        self._lock

    def locked(self):
        return self._lock.locked()

    def release(self):
#        print "released", self
        #traceback.print_tb
        self._lock.release()
    def __enter__(self):
        self.acquire()
    def __exit__(self, type, value, traceback):
        self.release()
#'''
def AllocLock():
#    return SafeLock()#str(uuid.uuid4()),100000,
#    return thread.allocate_lock()
	return threading.RLock()

def FixStrInt(s):
    return ''.join(filter(lambda c:c.isdigit(),list(s)))

def FixStrAlpha(s):
    return ''.join(filter(lambda c:c.isalpha(),list(s)))

class gMapInfo:
    def __init__(self):
        pass

def __gMap(defFunc, obj, info=None):

    if isinstance(obj,(tuple,list)):
        return map(lambda x: __gMap(defFunc,x,info),obj)

    if op.isMappingType(obj):
        for k,v in obj.items()[:]:
            del obj[k]
            obj[__gMap(defFunc,k,info)]=__gMap(defFunc,v,info)
        return obj

    return defFunc(obj)

def gMap(defFunc,obj):
    """gMap is extend map functionality by going deeper into {} and [] and call function for each element"""
    if not defFunc:
        return obj

    return __gMap(defFunc,obj,None)

def EncodeStr(obj, Enc, Dec=None):
    func=None
    if Enc and Dec:
        func=lambda s : (isinstance(s,(str,unicode)) and s.decode(Dec).encode(Enc)) or s
    elif Dec:
        func=lambda s : (isinstance(s,(str,unicode)) and s.decode(Dec)) or s
    elif Enc:
        func=lambda s : (isinstance(s,(str,unicode)) and s.encode(Enc)) or s

    if not func:
        return obj
    else:
        return gMap(func,obj)

def utf8(obj):
    return EncodeStrings(obj,'utf-8')
    #return gMap(lambda s : ((isinstance(s,unicode) and s.encode('utf8')) or s),obj)

def u8(obj):
    return utf8(obj)

print_lock = AllocLock()
def out(*args, **kwargs):
  with print_lock:
    print(*args)
#    ret=EncodeStrings(obj,'unicode')
#    print ret
#    return ret

class TrueDebug(object):
    ### Alpha ###
    """A simple debugger. Add debug() to a function and it prints the function name and any objects included.
    Adding True to locale prints the file name where the function is. Adding False to log turns the log off.
    This feature can be modified to trace deeper and find the bugs faster, ending the puzzle box."""
    def __init__(self, objects=None, locale=False, log=True, parents=False):
        if log == False: return
        current = inspect.currentframe()
        if parents: self.get_parents(current)
        self.true_debug(current, objects, locale)

    def true_debug(self, current, objects, locale):
        debug_string = 'Function: ' + str(inspect.getouterframes(current)[1][3])
        #if locale == 'all': print inspect.getouterframes(current)[4]; return
        if objects != None: debug_string += ' Objects: ' + str(objects)
        if locale: debug_string += ' File: ' + str(inspect.getouterframes(current)[1][1])
        out(debug_string)
        return

    def get_parents(self, current):
        debug_string = 'Function: ' + str(inspect.getouterframes(current)[1][3]) + ' Parents:'
        family = list(inspect.getouterframes(current))
        for parent in family:
            debug_string += ' ' + str(parent[4])
        out(debug_string)
        return
#debug = TrueDebug

def ListMinus(l1,l2):
    return list(sets.Set(l1).difference(l2))

conversion = {
        'а' : 'a',
        'б' : 'b',
        'в' : 'v',
        'г' : 'g',
        'д' : 'd',
        'е' : 'e',
        'ё' : 'e',
        'ж' : 'zh',
        'з' : 'z',
        'и' : 'i',
        'й' : 'j',
        'к' : 'k',
        'л' : 'l',
        'м' : 'm',
        'н' : 'n',
        'о' : 'o',
        'п' : 'p',
        'р' : 'r',
        'с' : 's',
        'т' : 't',
        'у' : 'u',
        'ф' : 'f',
        'х' : 'h',
        'ц' : 'c',
        'ч' : 'ch',
        'ш' : 'sh',
        'щ' : 'sch',
        'ь' : "_",
        'ы' : 'y',
        'ъ' : "_",
        'э' : 'e',
        'ю' : 'u',
        'я' : 'ja',
        'А' : 'A',
        'Б' : 'B',
        'В' : 'V',
        'Г' : 'G',
        'Д' : 'D',
        'Е' : 'E',
        'Ё' : 'E',
        'Ж' : 'ZH',
        'З' : 'Z',
        'И' : 'I',
        'Й' : 'J',
        'К' : 'K',
        'Л' : 'L',
        'М' : 'M',
        'Н' : 'N',
        'О' : 'O',
        'П' : 'P',
        'Р' : 'R',
        'С' : 'S',
        'Т' : 'T',
        'У' : 'U',
        'Ф' : 'F',
        'Х' : 'H',
        'Ц' : 'C',
        'Ч' : 'CH',
        'Ш' : 'SH',
        'Щ' : 'SCH',
        'Ъ' : "_",
        'Ы' : 'Y',
        'Ь' : "_",
        'Э' : 'E',
        'Ю' : 'U',
        'Я' : 'JA',
        }

rusAlf=conversion.keys()

conversionUnicode=EncodeStr(conversion,None,'utf-8')

def IsRus(s,flCheckAllSymbols=0):
    s=RusLower(s)
    for x in s:
        flRus=x in rusAlf
        if not flRus and flCheckAllSymbols:
            return False
        if flRus and not flCheckAllSymbols:
            return True

    return True

def IsEng(s, flCheckAllSymbols=0):
    for symb in s:
        so=ord(symb)
        flEng=((so>=65) and (so<90)) or ((so>=97) and (so<122))
        if not flEng and flCheckAllSymbols:
            return False
        if flEng and not flCheckAllSymbols:
            return True

    return True

def UnknownChar4File(c):
    if c.isalnum():
      return c
    else:
      return ' '

def cyr2lat(s,onUnknownChar=None,autoReplace={},flSkipQuotedStr=0):
    retval = ""
    quotes=0
    dobleqoutes=0
    # for utf8 split by 2 symbols
    #s=[s[x:x+2] for x in range(0,len(s),2)]
    s=s.decode('utf-8')
    for c in s:
        try:
            if c=="'":
                quotes+=1
            if c=='"':
                dobleqoutes+=1

            if flSkipQuotedStr and (quotes%2<>0 or dobleqoutes%2<>0):
                retval += c
                continue

            #c = conversion[c]
            if c in autoReplace:
                c=autoReplace[c]
            else:
                c = conversionUnicode[c]
        except KeyError:
            if onUnknownChar:
              c=onUnknownChar(c)
            pass
        retval += c
    return retval.encode('utf-8')

def lat2cyr(s):
    import translit
    return translit.zvuchene.lat2cyr(s)

#print cyr2lat('Журнал заказов')
#print lat2cyr('cheburashka')

rLow = 'абвгдежзийклмнопрстуфхцчшщъыьэюяё'
rUpp = rLow.upper()
rGlasn = list('аеийоуыэюяё')

flLogErrorsOnly=1
flFullLog=2
LogType=flLogErrorsOnly
flPythonMode=0

#sys.excepthook
#let's just take cur module dir/Up/and set applog
#CurDir=os.path.dirname(os.sys.executable)
CurDir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'applog')
AppName='app'

def AbsPath(FileName):
  if ':' in FileName:
        return FileName
  FileName=FileName.replace('\\','/')
  if FileName[0]=='/':
    FileName=FileName[1:]
  return os.path.join(CurDir,FileName).replace('\\','/')

def ParseArgV(flUpperCase=0):
##    global CommandLine
    CommandLine=SmartTypes.SmartDict()
    for arg in range(1,len(sys.argv)):
        try:
            parm=sys.argv[arg]
            #print arg, parm
            key=parm[parm.index('/')+1:parm.index('=')]
            val=parm[parm.index('=')+1:]
            if flUpperCase:
              key=key.upper()
            CommandLine[key]=val
        except:
            pass
    return CommandLine

def SetCurDir(DirDefault):
   if CurDir=='':
     CurDir=DirDefault

LogFileName=fileutils.StrChangeFileExt(AppName,'log')

def DelLog(NewLogFileName=LogFileName):
    fName=AbsPath(NewLogFileName)
    if os.path.exists(fName):
      os.remove(fName) #win32api.DeleteFile

def SetLogFileName(FileName):
    global LogFileName
    LogFileName=FileName

LogLineDelim='\n'

def NewLogLineDelim(NewDelim='\n\n'):
    global LogLineDelim
    LogLineDelim=NewDelim

logQueue=Queue.Queue()

#write logs in separate threads
flLogThread=1

def Log(Msg,NewLogFileName=LogFileName,flAddTime=1, flClearLog=0, flError=0):
    if LogErrors and not flError:
        return
    if MaxLogSize==0:
        return

    pars=(Msg,NewLogFileName,flAddTime,flClearLog,flError)
    if flLogThread:
        logQueue.put(pars)
    else:
        _Log(*pars)

def LogThread():
    while 1:
        _Log(*logQueue.get())

def _Log(Msg,NewLogFileName=LogFileName,flAddTime=1, flClearLog=0, flError=0):
    try:
        if ('/' in NewLogFileName) or ('\\' in NewLogFileName):
            LogFName=NewLogFileName
        else:
            LogFName=AbsPath('logs/'+NewLogFileName+'_'+time.strftime('%Y%m%d-%H.%M',time.localtime()))
            if os.path.exists(LogFName) and (os.stat(LogFName).st_size>MaxLogSize) and (MaxLogSize>0):
                os.remove(LogFName)
            if not isinstance(Msg,(str,)):
                Msg=str(Msg)

        fileutils.Save2File(LogFName,((flAddTime and (time.strftime('%Y%m%d-%H.%M.%S',time.localtime())+' : ')) or '')+Msg+LogLineDelim,((flClearLog and 'w') or 'a'))
    except:
        pass

logsPath=AbsPath('logs')
if not os.path.exists(logsPath):
    os.makedirs(logsPath)

if flLogThread:
    thread.start_new_thread(LogThread,())

def LogError(sAddText='',flRaise=0, NewLogFileName=LogFileName):
    global saddtmp
    saddtmp=''
    s=traceback.format_exc()+(sAddText and ('\n From Author : '+sAddText))
    #special for com object
    z=s.split(': (',1)
    sadd=''
    if len(z)>1:
        try:
            sadd=eval(('('+z[1]).strip())
            def ConcatStr(stmp):
                global saddtmp
                saddtmp+=str(utf8(stmp))+'\n'
                return stmp

            ApplyFunc2Vals(sadd,ConcatStr)
            sadd=saddtmp
#            print sadd
            #print sadd
            #print utf8(sadd)
        except:
            sadd=''

    Log(s+'\n'+sadd,NewLogFileName,flError=1)
    #print s
    if flRaise:
        raise BaseException(s)

def CreateDirs(DirList):
    for fName in DirList:
      ## Check : Full path or Part
      fName=((fName.find(':')+1) and fName) or os.path.join(CurDir,fName)
      if not os.path.exists(fName):
        os.makedirs(fName)

def GetFileVerInfo(fullFilePath, verbose=0):
    '''
    Uses FileVer to get file information.
    Args:
      fullFilePath: should be a path reachable from the current directory
    Returns:
      a tuple of strings for the value of the ProductVersion and the
      value of FileVersion
    '''
    pipe = 0
    inputLine = 'not blank'
    productVersionPattern = re.compile("\W*ProductVersion\W*(\S*)", re.I)
    fileVersionPattern = re.compile("\W*FileVersion\W*(\S*)", re.I)
    noFileVerPattern = re.compile("not recognized", re.I)
    dirPattern = re.compile('-----')
    productVersionString = ''
    fileVersionString = ''
    if verbose:
        out(fullFilePath)
    try:
        # need to quote the path name to handle filenames with spaces
        pipe = os.popen ('.\\filever.exe /v "%s"' % fullFilePath)
        # fileInfo will be a list of lines from the output of filever
        fileInfo = pipe.readlines()
        pipe.close()
    except:
        traceback.print_exc()
        raise "Could not run filever.  Make sure it is on your path"
    # look for size and date from first line
    try: fileDate = fileInfo[0][50:60]
    except: fileDate = 'unknown'
    try: fileSize = fileInfo[0][39:49]
    except: fileSize = 'unknown'
    # look for product and file version strings in the reminder of the
    # output from filever.exe
    for line in fileInfo[1:]:
        match = productVersionPattern.search(line)
        if match:
            productVersionString = match.group(1)
        match = fileVersionPattern.search(line)
        if match:
            fileVersionString = match.group(1)
    return (fileDate, fileSize, productVersionString, fileVersionString)

def RusLower(s, DefEnc='utf-8'):
    # process lists tuples etc with strings
    if not isinstance(s,(unicode,str,basestring)):
        return ApplyFunc2Vals(s, RusLower)

    if (s is None) or (len(s)==0):
      return ''
    if not isinstance(s,unicode):
      try:
        s=s.decode(DefEnc,errors='xmlcharrefreplace')
        #s=s.encode('cp1251')
        #s=s.encode('utf-8')
      except:
        err='RusLower.'
        try:
            err+=s
        except:
            pass
        LogError(err)

    return s.lower().encode(DefEnc,errors='xmlcharrefreplace')


    s = s.lower()
    sLst=list(s)
    for ind in xrange(len(sLst)):
        pos=rUpp.find(sLst[ind])
        if pos>=0:
            sLst[ind]=rLow[pos]
    return reduce(lambda ret,x: ret+x,sLst)

#print RusLower('Журнал за').decode('utf-8')

def RusUpper(s):
    if (s is None) or (len(s)==0):
      return ''
    if not isinstance(s,unicode):
      try:
        #s=s.encode('cp1251')
        s=s.decode('utf-8')
      except:
        pass

    return s.upper().encode('utf-8')

    s = s.lower()
    sLst=list(s)
    for ind in xrange(len(sLst)):
        pos=rLow.find(sLst[ind])
        if pos>=0:
            sLst[ind]=rUpp[pos]
    return reduce(lambda ret,x: ret+x,sLst)

def RusEnc(s,DefEnc='utf-8'):
    if (s is None) or (len(s)==0):
      return ''
    if isinstance(s,unicode):
      try:
#        s=s.encode('cp1251')
        s=s.encode(DefEnc,errors='xmlcharrefreplace')
      except:
        err='RusEnc.'
        try:
            err+=s
        except:
            pass
        LogError(err)

    return s

def PickleObj(fName,Obj):
    fName=AbsPath(fName)
#    if os.path.exists(fName):
    f=open(AbsPath(fName),'wb')
    z=pickle.Pickler(f)
    z.dump(Obj)
    f.close()

def UnpickleObj(fName, Def=None):
    fName=AbsPath(fName)
    if os.path.exists(fName):
        f=open(fName,'rb')
        ret=pickle.load(f)
        f.close()
        return ret
    return Def

class AnyData2PickleFile:
    def __init__(self,filename):
        self.filename=filename

    def __call__(self,data):
        PickleObj(self.filename,data)

class AnyData2Csv:
    def __init__(self,filename,fieldSeparator=';',lineSeparator='\n'):
        self.filename=filename
        self.fieldSeparator=fieldSeparator
        self.lineSeparator=lineSeparator

    def __call__(self,data):
        fileutils.Save2Csv(self.filename,data,self.fieldSeparator,self.lineSeparator)

def CallOrReturn(funcOrValue,*argv,**kwargs):
    return (not callable(funcOrValue) and funcOrValue) or funcOrValue(*argv,**kwargs)

class DefFuncParam():
    """Run user defined function (lambda for example) with any params.
Default order :
  Noname params add to call params (at end),
  Named params will be updated with call params
"""
    def __init__(self,func,*argv,**kwargs):
        self.func=func
        self.argv,self.kwargs=argv,kwargs

    def __call__(self,*argv,**kwargs):
        kw=self.kwargs
        kw.update(kwargs)
        return self.func(*(self.argv+argv),**kw)

def my_excepthook(type, value, tback):
    # log the exception here
#    curframe = inspect.currentframe()
#    calframe = inspect.getouterframes(curframe, 10)
#    if len(calframe)>10:
#        return
    Log(''.join(traceback.format_exception(type, value, tback, limit=None)))
#    'Exception : \ntype=%s value=%s tback=%s'%())
    # then call the default handler
    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook

class Params():
    def __init__(self,FileName=fileutils.StrChangeFileExt(AppName,'ini')):
        # get command lines params to override ini params
        cmdPars=ParseArgV()

        FileName=AbsPath(FileName)
        ret=[]
        if os.path.exists(FileName):
            f=open(FileName,'r')
            try:
                ret=f.readlines()
            finally:
                f.close()

        iniPars=SmartTypes.SmartDict()
        def getVal(val):
            # check for const values
            v=val
            try:
                v=eval(val)
                if not isinstance(v,(int,float,list,tuple,type(Log))):
                    v=val
            except:
                v=val
            return v

        for x in ret:
            z=map(lambda s : s.strip(),x.split('=',1))
            if not z or len(z)<>2 or z[0].strip().startswith('#'):
                continue

            iniPars[z[0]]=z[1]


#        print 'cmdPars',cmdPars
#        print 'iniPars',iniPars
        iniPars.update(cmdPars)
        for k,v in iniPars.items():
#            print k,v
            v=getVal(v)
            setattr(self,k,v)

#print 'Params'
params=Params()
fLockThread=AllocLock()
LogErrors=getattr(params,'LogErrors',0)
MaxLogSize=getattr(params,'MaxLogSize',10*1000*1000)

arrVal=lambda x : (isinstance(x,(tuple,list)) and (((len(x)==1) and arrVal(x[0])) or ((len(x)>1) and map(arrVal,x)))) or x or ''
#test=[1,[[1]],[],[[[1,[2,3]]]]]
#test1=arrVal(test)

def ArrTree2OneDimArr(arr,flMaxSeqOnly=1):
    ret=__ArrTree2OneDimArr(arrVal([arr]),[],[])
    if flMaxSeqOnly:
        lMax=len(max(ret,key=len))
        ret=filter(lambda x : len(x)==lMax,ret)
    return ret
"""
lst=[[[[50775208],
   [[[[[50790752], [[50674536]]],
      [[50790432], [[44939664]]],
      ]]]],
  [[50785120],
   [[[[[46977176], [[50734032]]],
      [[50709680], [[50608984]]],
      ]]]]]]

#def MyTree(arr, ret=[]):
#   if isinstance(arr,(tuple,list)):
#        return MyTree()

#obj1=arrVal([lst])
print ArrTree2OneDimArr(lst)
"""
def __ArrTree2OneDimArr(arr,buf=[],res=[]):
    #if not isinstance(x,(tuple,list)):
    #    buf

    # check if not list at all
    if not isinstance(arr,(tuple,list)):
      res.append(arr)
      return res

#if list then go deeper
    l=len(arr)
    for i in xrange(len(arr)):
        v=arr[i]
        if isinstance(v,(tuple,list)):
            __ArrTree2OneDimArr(v,buf[:],res)
            #map(lambda x: ArrTree2OneDimArr([x]+(((i+1)<l and arr[i+1:]) or []),buf[:],res),v)
            #return res
        else:
            buf.append(v)
    res.append(buf)
    return res

#a=['Гвозди', ['Гвозди строительные - ГОСТ 4028-63','<table bordep></td>\n</tr></table>']]
#print ArrTree2OneDimArr(a)

def removeComments(s, flStrictSingleLine=0):
    s='\n'+s+'\n'
    s=re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,s) # remove all occurance streamed comments (/*COMMENT */) from string
#^//.*?\$
    s=re.sub(re.compile("^[ ]*//.*?\n", re.MULTILINE+re.DOTALL) ,"" ,s) # remove all occurance singleline comments (//COMMENT\n ) from string
    s=re.sub(re.compile("^[ ]*#.*?\n", re.MULTILINE+re.DOTALL) ,"" ,s) # remove all occurance singleline comments (#COMMENT\n ) from string
    s=re.sub(re.compile("^[ ]*--.*?\n", re.MULTILINE+re.DOTALL) ,"" ,s) # remove all occurance singleline comments (--COMMENT\n ) from string
    if not flStrictSingleLine:
        s=re.sub(re.compile("//.*?\n" ) ,"\n" ,s) # remove all occurance singleline comments (//COMMENT\n ) from string
        s=re.sub(re.compile("#.*?\n" ) ,"\n" ,s) # remove all occurance singleline comments (#COMMENT\n ) from string
        s=re.sub(re.compile("--.*?\n" ) ,"\n" ,s) # remove all occurance singleline comments (--COMMENT\n ) from string

    if 'exit()' in s:
        d=s.split('exit()')
        s=d[0]

    return s

def striplines(s):
    s=re.sub(re.compile("^[  ].*?\n", re.MULTILINE+re.DOTALL) ,"\n" ,s)
#    s=re.sub(re.compile("" ) ,"\n" ,s)
    return s

def ApplyFunc2Vals(vals, func):
    """
    func(val,key=None,ind=None)
     trying to apply func to array or list or dict or string or any other types.
    """
    try:
        if isinstance(vals,(str,unicode)):
            return func(vals)
        elif hasattr(vals,'items'):#isinstance(vals,(dict)) or
            cl=vals.__class__
            return cl([[ApplyFunc2Vals(k,func),ApplyFunc2Vals(v,func)] for k,v in vals.items()])
        elif isinstance(vals,(list,tuple)):
            cl=vals.__class__
            return cl(map(lambda x : ApplyFunc2Vals(x,func),vals))
        else:
            return func(vals)
    except:
        LogError(str(vals),1)

from chardet.latin1prober import Latin1Prober # windows-1252
from chardet.utf8prober import UTF8Prober
from chardet.sbcharsetprober import SingleByteCharSetProber
from chardet.langcyrillicmodel import Win1251CyrillicModel, Koi8rModel, Latin5CyrillicModel, MacCyrillicModel, Ibm866Model, Ibm855Model

def DetectEncoding(s,Def='utf-8'):
#    codecs=[UTF8Prober(),Latin1Prober()]#,SingleByteCharSetProber(Win1251CyrillicModel),SingleByteCharSetProber(Koi8rModel),SingleByteCharSetProber(MacCyrillicModel)]
#    ret=[x.feed(s).close() for x in codecs]
#    ret=ret and ret[0]
    ret=chardet.detect(s)
    if ret and (ret['confidence']>0.5):
        return ret['encoding']
    return Def
#DetectEncoding('kjhdfkjhas')

def __EncodeStrings(v,Encode='utf-8'):
    if (not isinstance(v,(str,unicode))) and (isinstance(v,(list,tuple)) or  hasattr(v,'items')):
        return ApplyFunc2Vals(v,DefFuncParam(__EncodeStrings,Encode=Encode))

    if isinstance(v,str):
        if (not local.EncodeStrings_Decode) or (local.EncodeStrings_Decode=='ascii'):
            local.EncodeStrings_Decode=DetectEncoding(v)

        if (local.EncodeStrings_Decode!=Encode):
#            try:
            v=v.decode(local.EncodeStrings_Decode)
            if Encode!='unicode':
                return v.encode(Encode)#,'xmlcharreplace'
#            except:
#                pass
            return v
        return v
    elif isinstance(v,unicode):
        if Encode!='unicode':
            v=v.encode(Encode)
    else:
        if Encode=='unicode':
            v=unicode(v)
        else:
            v=str(v)

    return v

def EncodeStrings(v,Encode='utf-8'):
    local.EncodeStrings_Decode=None
    return __EncodeStrings(v,Encode)

def cache(KeyObj,Obj=None,cacheExt='.html',cacheLocation='cache'):
    return ''
    cacheLocation=AbsPath(cacheLocation)
    hash = md5.new(str(KeyObj)).hexdigest()
    cacheFile=cacheLocation + "/" + hash + cacheExt

    if Obj is None:
        if os.path.exists(cacheFile):
            ret=GetFileData(cacheFile,0,'rb')
            return ret
        else:
            return ''
    else:
        if not os.path.exists(cacheLocation):
            os.mkdir(cacheLocation)
#        ret=str(Obj)
        fileutils.Save2File(cacheFile,str(Obj),'wb')
        return Obj

def say(s, flPrint=1):
    if flPrint:
        out(s)
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    lang=''
    if IsRus(s) or s.isdigit():
        s=EncodeStrings(s,'cp1251')
        lang='ru'
    subprocess.check_output([r'say.bat',s,lang],startupinfo=startupinfo)

def GetCurIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip=s.getsockname()[0]
    s.close()
    return ip

RecvList=Queue.Queue()
SendList={}

#lockRecv=AllocLock()
##lockSend=AllocLock()

def _ListenPort(port=8765, ip=None, check_proc=None):
    backlog=100
    if not ip:
        ip=GetCurIp()
    #address = (ip, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip,port))
    inputs = [server]
    addresses={}
    out('Listening to port',port,'...')
    server.listen(backlog)
    while True:
        try:
            inputready,outputready,exceptready = select.select(inputs, [], [])
        except select.error, e:
            app.LogError()
            break
        except socket.error, e:
            app.LogError()
            break

        for sCl in inputready:
            if sCl == server:
                # handle the server socket
                client, address = server.accept()
                out('got connection %d from %s' % (client.fileno(), address))
                # Read the login name
                # Compute client name and send back
#                    send(client, 'CLIENT: ' + str(address[0]))
                try:
                    local_addr = communication.receive(client)
                    communication.send(client, '')
                    addresses[hash(client)]=(local_addr,address[-1])
                    out(local_addr)
                    inputs.append(client)
                except socket.error, e:
                    LogError('receive address error',0,'conn_err.log')
                    try:
                        client.close()
                    except:
                        LogError('receive address error on client.close()',0,'conn_err.log')
            else:
                # handle all other sockets
                try:
                    # data = s.recv(BUFSIZ)
                    adr=addresses[hash(sCl)]

                    ip=adr[0]
                    if ip not in SendList:
                        SendList[ip]=Queue.Queue()

                    Log('Start Recv','conn.log')
                    data = communication.receive(sCl)
                    if not data:
                        data=''
                        Log('EmptyData %s : %s'%(str(adr),data),'conn.log')
                        continue
#                    Log('onData %s : %s'%(str(adr),data),'alldata.log')

                    # addtitional transport check
                    if check_proc:
                        check_proc(data)

                    RecvList.put((data,adr))
#                    except:
#                        LogError('Critical error :(RecvList.put)  %s : %s'%(str(adr),data),0,'conn.log')

                    Log('Recv %s : %s'%(str(adr),data),'conn.log')

                    val=''
##                    try:
##                      val=SendList[ip].get_nowait()
##                      # not our time, leave it for now, and send ''
##                      if datetime.datetime.now()<val[1]:
##                        SendList[ip].put(val)
##                        val=''
##                      else:
##                        val=val[0]
##                    except:
##                        pass
                    try:
                        val=SendList[ip].get_nowait()
                        if not val:
                            val=''
                    except:
                        val=''

                    if not val:
                        val=''

                    try:
                        communication.send(sCl,val)
#                        Log('onData Answer %s : %s'%(str(adr),val),'alldata.log')
#                        Log('Sent %s : %s'%(val,data),'conn.log')
                    except:
                        # not sent, repeat
                        if val<>'':
                            SendAnswer(val,ip)
                        LogError('OnMsg %s : %s'%(str(adr),val),0,'conn_err.log')
                except socket.error, e:
                    LogError('ListenPort',0,'conn_err.log')
                    try:
                        sCl.close()
                    except:
                        LogError('ListenPort on Safe Close Socket',0,'conn_err.log')
                    try:
                        inputs.remove(sCl)
                        sCl=None
                    except:
                        LogError('ListenPort on Safe remove client',0,'conn_err.log')

    server.close()

def ListenPort(OnMsg,port=8765, ip=None, check_proc=None, warn_proc=None):
    thread.start_new_thread(_ListenPort, (port,ip,check_proc))
    while True:
        v,adr=RecvList.get()
        try:
            tStart=now()
            OnMsg(v,adr)#,RecvList.empty()
            tEnd=now()
            if warn_proc:
                tDelta=(tEnd-tStart).total_seconds()
                if tDelta>0.1:
                    err_msg='MyMsg : ExecTime=%s; Adr=%s; Msg=%s'%(tDelta,str(adr),v)
                    warn_proc(err_msg)
        except:
            err_msg='OnMsg %s : %s'%(str(adr),v)
            if warn_proc:
                warn_proc(err_msg)
            LogError(err_msg,0,'conn_err.log')

def SendAnswer(msg,ip,wait=0):
    try:
        if msg.strip()<>'':
            SendList[ip].put(msg.strip())
    except:
        pass
#        SendList[ip].put((msg.strip(),datetime.datetime.now()+datetime.timedelta(0,wait)))

#print removeComments('Tes\n#t1')
'''
s="""
Test // dsjfkajh
Tes#t1
  //1312312
sss
222 #HHH

11/*
long comments
*/
"""
print removeComments(s)
print striplines(s)
'''

#print utf8({'qdwqe':[34,5436,'gfdshgsd']})