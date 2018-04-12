##import win32api
import thread,threading,time
import utils.apputils
from utils import apputils,fileutils
import traceback
import sys, uuid, os
##rmutex = thread.allocate_lock() # for calls to random
flOneThreadMode=0#(__debug__ and 1) or 0
CleanUpFunc=None

LogLocation=apputils.AbsPath('log')
if not os.path.exists(LogLocation):
    os.mkdir(LogLocation)

def SimpleLog(msg):
    if utils.apputils.LogType==utils.apputils.flLogErrorsOnly:
        return
    fname=apputils.AbsPath('log\\'+str(uuid.uuid4())+'.txt')
    f=open(fname,'wb')
    f.write(msg)
    f.close()

class ThreadExcept:
  def __init__(self):
    self.error=traceback.format_exc()
    self.exception=sys.exc_info()[1]
#    print 'Exception : ', str(self)
#    SimpleLog(str(self))
    if flOneThreadMode:
        apputils.Log(str(self))
#        print 'Exception : ', str(self)
  def __str__(self):
    return str(self.error)+' '+str(self.exception)

##try:
##  a=1/0
##except:
##  b=ThreadExcept()
##  print str(b)

#exit(0)
FullLogFileName='Threads.log'

class ThreadObj:
  pass

loc=threading.local()

def DoCleanUp():
    try:
        if CleanUpFunc:
            CleanUpFunc()
    except:
        apputils.LogError('Threads CleanUpFunc error')


class Threads:
  def __init__(self, RepeatIfExcept=1, MaxThreadCount=256, flLog=apputils.LogType, flNoResult=0):  #, OnError=None):
    global loc
    self.MaxThreadCount=MaxThreadCount
    self.mutex = threading.Lock()
    self.running = 0
    self.ReturnData={}
    self.done = threading.Lock()
    self.RepeatIfExcept=RepeatIfExcept
    self.flLog=flLog
    if not getattr(loc,'obj',None):
        loc.obj=ThreadObj()
    self.curThread=loc.obj
    self.flNoResult=flNoResult
##    self.OnError=OnError
##    self.done.acquire()
  def MutexAcquire(self):
    if not flOneThreadMode:
      self.mutex.acquire()

  def MutexRelease(self):
    if not flOneThreadMode:
      self.mutex.release()

  def __task(self,index, func,args, kwargs):
    global loc
    try:
      fResult=None
      loc.obj=ThreadObj()
      loc.obj.parent=self.curThread
      rep,flDone=0,0
      while (rep<=self.RepeatIfExcept) and (not flDone):
        rep+=1
        try:
          # log all tasks params
          if self.flLog==apputils.flFullLog:
            apputils.Log((';params;'+func.__name__+'('+str(args)+')').replace('\n','\\'),FullLogFileName)
          fResult=func(*args,**kwargs)
          flDone=1
        except (KeyboardInterrupt, SystemExit):
          sys.exit(0)
        except:
          fResult=ThreadExcept()
          apputils.LogError('Threads.__task'+str(func)+'\n'+str(args),str(kwargs))

        if self.flNoResult:
            fResult=None

        DoCleanUp()
##          if self.OnError:
##            try:
##              self.OnError(fResult)
##            except:
##              pass
    finally:
      self.MutexAcquire()
      self.running -= 1
      try:
        # log all tasks
        if self.flLog==apputils.flFullLog:
          apputils.Log((';'+((isinstance(fResult,ThreadExcept) and 'error') or 'success')+';'+str(fResult)).replace('\n','\\'),FullLogFileName)

        # check for auto error log
        if self.flLog and isinstance(fResult,ThreadExcept):
          #log all Errors
          apputils.Log(str(fResult.exception)+'\n'+fResult.error+'\nfunction params='+str(args)+str(kwargs))
          self.ReturnData[index]=None
        else:
          self.ReturnData[index]=fResult

        DoCleanUp()
      finally:
        if self.running == 0 and self.IsLocked():
          self.done.release()
        self.MutexRelease()

  def ActiveCount(self):
    self.MutexAcquire()
    try:
      return self.running
    finally:
      self.MutexRelease()

  def NewThread(self, func, *args, **kwargs):
    global flOneThreadMode
    ## Limit for threads count
    if self.ActiveCount()>=self.MaxThreadCount:
      self.WaitThreads()

    if not self.done.locked():
      self.done.acquire()
    if type(args) not in (type(tuple()),type(list())):
      args=(args,)
    else:
      args=tuple(args)

    if type(args) != type(tuple()):
        raise TypeError("2nd arg must be a tuple")
    if type(kwargs) != type(dict()):
        raise TypeError("3rd arg must be a dict")

    self.MutexAcquire()
    try:
      self.running += 1
      index=len(self.ReturnData.keys())
      self.ReturnData[index]=None
      while 1:
        try:
            if flOneThreadMode:
                self.__task(index,func, args, kwargs)
            else:
                thread.start_new_thread(self.__task, (index,func, args, kwargs))
            break
        except:
##          if win32api.GetLastError()==8:# not enough memory
##            time.sle ep(20)
##          else:
            raise
    finally:
      self.MutexRelease()

  def NewThreads(self, func, arglist):
    argcount=func.func_code.co_argcount
    if not arglist:
      self.NewThread(func)
      return
    for x in arglist:
      if (argcount==1) or not isinstance(x,(list,tuple)):
        self.NewThread(func,x)
      else:
        self.NewThread(func,*x)

  def IsLocked(self):
    return self.done.locked()

  def WaitThreads(self):
    self.done.acquire()

  @classmethod
  def StartAndWait(cls,func,argslist,RepeatIfExcept=1, MaxThreadCount=256, flLog=apputils.LogType, flNoResult=0): #, OnError=None):flRemoveErrors=True
    tList=Threads(RepeatIfExcept, MaxThreadCount, flLog,flNoResult) #, OnError)
    tList.NewThreads(func,argslist)
    tList.WaitThreads()
    ret=tList.ReturnData
#    if flRemoveErrors:
#        ret=filter(lambda k,v: not isinstance(v,ThreadExcept),ret.items())
    del tList
    return ret

class ClassThreadParams():

    class EmptyClass():
        pass

    def __init__(self):
      self.lock=threading.Lock()
      self.threads={}

    def __getCurItem(self,instance):
        global loc
        cur=loc.obj
        while 1:
            if cur in self.threads.keys() and hasattr(self.threads[cur],instance):
                return cur
            if not hasattr(cur,'parent'):
                return None
            cur=cur.parent
        #eval('self.'+instance)

    def __get__( self, instance, owner):
        self.lock.acquire()
        try:
          cur=self.__getCurItem(instance)
          if not cur:
            raise 'ThreadParams.__getCurItem('+instance+')'
          return getattr(self.threads[cur],name)
        finally:
            self.lock.release()

    def __set__( self, instance, value):
        global loc
        self.lock.acquire()
        try:
          cur=self.__getCurItem(instance)
          if not cur:
            self.threads[loc.obj]=EmptyClass()
            setattr(self.threads[self.__getCurItem(instance)],instance,value)
          else:
            return setattr(self.threads[self.__getCurItem(instance)],instance,value)
        finally:
            self.lock.release()

ThreadParams=ClassThreadParams()
exec_threads=Threads.StartAndWait