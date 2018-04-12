# coding=utf-8
import distutils.filelist
import threading
import os,sys
import time
import tempfile
import datetime
#import win32file
import codecs
import string,unicodedata

#fl=distutils.filelist.findall(r'c:\PICS')
#fd=os.open(FileName,0)
#stat=os.fstat(fd)
#map(lambda fname, stat : {'CreateDt': time.strftime(TimeMask,time.localtime(stat[9])),'ModifyDt' : time.strftime(TimeMask,time.localtime(stat[8])),'FSize':stat[6]},
TimeMask='%d.%m.%Y %H.%M.%S'

##def FileExist(FileName):
##    return os.path.exists(FileName)

FILE_ATTRIBUTE_READONLY = 1
FILE_ATTRIBUTE_HIDDEN = 2
FILE_ATTRIBUTE_SYSTEM = 4
FILE_ATTRIBUTE_DIRECTORY = 16
FILE_ATTRIBUTE_ARCHIVE = 32
FILE_ATTRIBUTE_NORMAL = 128
FILE_ATTRIBUTE_TEMPORARY = 256


validFilenameChars = "$-_.() %s%s" % (string.ascii_letters, string.digits)

def removeDisallowedFilenameChars(filename):
#    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(c for c in filename if c in validFilenameChars)

#print removeDisallowedFilenameChars('4ffgsdags')

class FileNameInfo:
    def __init__(self,FileName):
        self.Name=FileName
        self.ShortName=os.path.basename(FileName)
        self.Ext=FileName[FileName.rfind('.')+1:]
        self.WithoutExt=self.ShortName[:self.ShortName.rfind('.')]

    #    self.Attributes=win32file.GetFileAttributes(self.Name)
    #    self.isReadonly= self.Attributes & win32file.FILE_ATTRIBUTE_READONLY
    #    self.isHidden= self.Attributes & win32file.FILE_ATTRIBUTE_HIDDEN
    #    self.isSystem= self.Attributes & win32file.FILE_ATTRIBUTE_SYSTEM
    #    self.isDir= self.Attributes & win32file.FILE_ATTRIBUTE_DIRECTORY
    #    self.isArchive= self.Attributes & win32file.FILE_ATTRIBUTE_ARCHIVE
    #    self.isNormal= self.Attributes & win32file.FILE_ATTRIBUTE_NORMAL
    #    self.isTemporary= self.Attributes & win32file.FILE_ATTRIBUTE_TEMPORARY

def CreateDirs(Path):
    Path=apputils.AbsPath(Path)
    if not os.path.exists(Path):
        os.makedirs(Path)

def GetFileList(Path,Ext='*'):
    ret=[]
    if not os.path.exists(Path):
        return ret
    for fName in distutils.filelist.findall(Path):
        f=FileNameInfo(fName)
        if (Ext=='*') or (f.Ext.lower()==Ext.lower()):
            ret.append(f)
    return ret

def ClearDir(Path):
    lst=GetFileList(Path)
    for f in lst:
        os.remove(f.Name) #win32api.DeleteFile(f.Name)

def GetFileInfo(fPath):
    try:
        fd=os.open(fPath,0)
        stat=os.fstat(fd)
        ret={'CreateDt': time.strftime(TimeMask,time.localtime(stat[9])),'ModifyDt' : time.strftime(TimeMask,time.localtime(stat[8])),'ModifyDate':datetime.datetime.fromtimestamp(stat[8]),'FSize':stat[6]}
        os.close(fd)
        return ret
    except:
        return None


def GetFilesInfo(Path):
    fl=distutils.filelist.findall(Path)
    ret={};
    for f in fl:
        ret[f]=GetFileInfo(f)
    return ret


#def ToHist(fName):
#    Save2File('hist')
    #apputils.AbsPath(fName)

##def GetFileExt(FileName):
##    return FileName[FileName.rfind('.')+1:].upper()

## replace file extension from .<ext> to .<NewExt>
def StrChangeFileExt(FileName,NewExt):
    """
    Example : StrChangeFileExt(FileName='1.txt',NewExt='py')
      set new extesion for file.
    """
    return FileName[:FileName.rfind('.')+1]+NewExt

def StrChangeFileName(FullFileName,NewFileName):
    if ':' in NewFileName:
        NewFileName=os.path.basename(NewFileName)
    return FullFileName[:FullFileName.rindex('\\')+1]+NewFileName

def ChangeFileName(FullFileName,NewFileName):
    os.rename(FullFileName,StrChangeFileName(FullFileName,NewFileName));

def OpenTextFile(filename, mode='r', encoding = None):
    hasBOM = False
    skipBytes=0
    if os.path.isfile(filename):
        f = open(filename,'rb')
        header = f.read(4)
        f.close()

		# Don't change this to a map, because it is ordered
        encodings = [ ( codecs.BOM_UTF32, 'utf-32' ),
			( codecs.BOM_UTF16, 'utf-16' ),
			( codecs.BOM_UTF8, 'utf-8' ) ]

        for h, e in encodings:
            if header.startswith(h):
                skipBytes=len(h)
                encoding = e
                hasBOM = True
                break

#    if encoding:
#        f = codecs.open(filename,mode,encoding)
#    else:
    f = open(filename,mode)
	# Eat the byte order mark
    if skipBytes:
        f.read(skipBytes)
#	if hasBOM:
#		f.read(1)
    return f

def GetFileData(FileName, flStrList=0, Mode='r', Encoding=None, SafeCall=1):
    FileName=apputils.AbsPath(FileName)

    if not os.path.exists(FileName):
        if SafeCall:
            if flStrList:
                return []
            return ''
        else:
            raise Exception('GetFileData. FileName=%s is not found'%FileName)

    f=OpenTextFile(FileName,Mode,Encoding)
    try:
      if flStrList:
          return f.readlines()
      else:
          return f.read()
    finally:
      f.close()

def GetCsvData(FileName,fieldSeparator=';',lineSeparator='\r\n'):
    import csv
    ret=csv.reader(open(apputils.AbsPath(FileName), 'rb'), delimiter=fieldSeparator, quotechar='"')
    return list(ret)

def Save2File(FileName,Text,Mode='w',enc=None):
    FileName=apputils.AbsPath(FileName)

    if enc:
        f=codecs.open(FileName,Mode,enc,'backslashreplace',1000000)
    else:
        f=open(FileName,Mode)
    try:
        if hasattr(Text,'__iter__'):
            Text='\n'.join(Text)
            #f.writelines(Text)
        #else
        if isinstance(Text,unicode):
            Text=Text.encode(enc or 'utf-8')

        f.write(Text)
    except:
        raise
        pass
        #import apputils
        #apputils.LogError(FileName,1)
##        # if characters error then trying to save with errors replace
##        if hasattr(sys.exc_info()[1],'reason') and (sys.exc_info()[1].reason.find('character maps')>=0):
##            f.close()
##            f=codecs.open(FileName,Mode,'cp1251','replace')
##            if hasattr(Text,'__iter__'):
##                f.writelines(Text)
##            else:
##                f.write(Text)
##        else:
##            raise;

    f.close()

def ToUtf8(s):
    if isinstance(s,(str,)):
        return s #unicode(s.decode('cp1251'))

    if isinstance(s,(unicode,)):
        return s.encode('utf8')

    return str(s)

lineSep=lambda lst,sep : reduce(lambda ret,x: ret+ToUtf8(x)+sep,lst,'')[:-1]

#lineSep=lambda lst,sep : reduce(lambda ret,x: ret+ToUnicodeStr(x).replace(sep,u' ')+sep,lst,u'')[:-1]

def utf_8_encoder(unicode_csv_data):
    for row in unicode_csv_data:
        yield [(isinstance(s,unicode) and s.encode("utf-8")) or s for s in row]

def CsvFromArr(lst,fieldSeparator=';',lineSeparator='\r\n'):
    return reduce(lambda ret,x: ret+lineSep(x,fieldSeparator).replace(lineSeparator,' ')+lineSeparator,lst,'')

def Save2Csv(FileName,DataArr,fieldSeparator=';',lineSeparator='\r\n',enc='utf8'):
    import csv
#    apputils.Log(str(DataArr),'Save2Csv.log')
    if not DataArr or not DataArr[0]:
        return
#    arr=DataArr
    arr=apputils.EncodeStrings(DataArr,'utf-8')
#    if len(DataArr)>1 and DataArr[1]:
#        test
#    if any(map(lambda s : isinstance(s,unicode),DataArr[0]+)):
#        arr=utf_8_encoder(DataArr)
    with open(apputils.AbsPath(FileName), 'wb') as f:
        writer=csv.writer(f, delimiter=';',escapechar='\\',quoting=csv.QUOTE_NONE,lineterminator=lineSeparator)
        writer.writerows(arr)

def Save2Csv_old(FileName,DataArr,fieldSeparator=';',lineSeparator='\r\n',enc='utf8', add_repl=lambda s : s):
    data=lineSeparator.join([fieldSeparator.join([add_repl(ToUtf8(f or '')).replace(lineSeparator,' ').replace(fieldSeparator,' ') for f in l]) for l in DataArr])
#ToUtf8(f)
    if enc<>'utf8':
        data=data.decode('utf8').encode(enc)

    Save2File(FileName,data,'w')
    #decode('cp1251').


def RenFiles_DateName(Path):
    try:
      fl=GetFilesInfo(Path);
      for f,i in fl.items():
          print f
          ChangeFileName(f,i['CreateDt']+'.'+GetFileExt(f))
    except:
        None

##def GetUniqueFileName():
##    return time.strftime('%Y%m%d-%H_%M_%S',time.localtime())

def GetTempFilename(suffix='',prefix='', dir=tempfile.gettempdir()):
    f=tempfile.TemporaryFile('w', suffix=suffix,prefix=prefix,dir=dir);
    ret=f.name
    f.close()
    return ret

def ConvertFileListToDict(FileList):
    ret={}
    for v in FileList:
        FName=v[v.rfind('\\')+1:].upper()
        ret[FName]=v
    return ret

def StoreOnFtp(SrcName,DstName,Server,User='mcs',Password='mcs'):
    import ftplib
    ftp=ftplib.FTP(Server,User,Password)
    ftp.storbinary('STOR '+DstName,open(SrcName,'rb'))
    ftp.close()

#print OpendFileDlg('pdf')
def OpendFileDlg(DefExt='*'):
    import apputils,win32gui,win32con
    try:
        flt='Other file types\0*.*\0'
        customfilter='%s\0*.%s\0'%(DefExt.upper(),DefExt)
        #fname, customfilter, flags
        return win32gui.GetOpenFileNameW(
            InitialDir=apputils.CurDir,
            Flags=win32con.OFN_EXPLORER,
          #  win32con.OFN_ALLOWMULTISELECT|
            File='', DefExt=DefExt,
            Title='GetOpenFileNameW',
            Filter=flt,
            CustomFilter=customfilter,
            FilterIndex=0)
    except:
        return None

class AnyData2File():
    def __init__(self,filename, flRewrite=1):
        self.filename=filename
        self.flRewrite=flRewrite

    def __call__(self,data):
        Save2File(self.filename,data)


"""Working example of the ReadDirectoryChanges API which will
 track changes made to a directory. Can either be run from a
 command-line, with a comma-separated list of paths to watch,
 or used as a module, either via the watch_path generator or
 via the Watcher threads, one thread per path.

Examples:
  watch_directory.py c:/temp,r:/images

or:
  import watch_directory
  for file_type, filename, action in watch_directory.watch_path ("c:/temp"):
    print filename, action

or:
  import watch_directory
  import Queue
  file_changes = Queue.Queue ()
  for pathname in ["c:/temp", "r:/goldent/temp"]:
    watch_directory.Watcher (pathname, file_changes)

  while 1:
    file_type, filename, action = file_changes.get ()
    print file_type, filename, action

(c) Tim Golden - mail at timgolden.me.uk 5th June 2009
Licensed under the (GPL-compatible) MIT License:
http://www.opensource.org/licenses/mit-license.php
"""
#from __future__ import generators
#import threading
#import time


ACTIONS = {
  1 : "Created",
  2 : "Deleted",
  3 : "Updated",
  4 : "Renamed to something",
  5 : "Renamed from something"
}

def watch_path(path_to_watch, include_subdirectories=False):
  import win32file
  import win32con
  FILE_LIST_DIRECTORY = 0x0001
  hDir = win32file.CreateFile (
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
  )
  while 1:
    results = win32file.ReadDirectoryChangesW (
      hDir,
      1024,
      include_subdirectories,
      win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
       win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
       win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
       win32con.FILE_NOTIFY_CHANGE_SIZE |
       win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
       win32con.FILE_NOTIFY_CHANGE_SECURITY,
      None,
      None
    )
    for action, file in results:
      full_filename = os.path.join (path_to_watch, file)
      if not os.path.exists (full_filename):
        file_type = "<deleted>"
      elif os.path.isdir (full_filename):
        file_type = 'folder'
      else:
        file_type = 'file'
      yield (file_type, full_filename, ACTIONS.get (action, "Unknown"))

class Watcher (threading.Thread):

  def __init__ (self, path_to_watch, results_queue, **kwds):
    threading.Thread.__init__ (self, **kwds)
    self.setDaemon (1)
    self.path_to_watch = path_to_watch
    self.results_queue = results_queue
    self.start()

  def run (self):
    for result in watch_path (self.path_to_watch,True):
      self.results_queue.put (result)

import apputils
