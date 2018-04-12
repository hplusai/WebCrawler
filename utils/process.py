import win32event
import win32process
import win32security

def ExecCommandLine(CommandLine,CreationFlags=0,flWait=0):
  sInfo=win32process.STARTUPINFO()
  pi=win32process.CreateProcess(
                           None,##appName
                           CommandLine,##commandLine
                           None,##processAttributes
                           None,##threadAttributes ,
                           0,##bInheritHandles ,
                           CreationFlags,##dwCreationFlags ,
                           None,##newEnvironment ,
                           None,##currentDirectory ,
                           sInfo##startupinfo
                               )
  hProcess,hThread,ProcessId,ThreadId=pi
  if flWait:
    win32event.WaitForSingleObject(hProcess, win32event.INFINITE );
  hProcess.Close()
  hThread.Close()


def ExecCommandLineNoShow(CommandLine,flWait=1):
  ExecCommandLine(CommandLine,win32process.CREATE_NO_WINDOW,flWait)