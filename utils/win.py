# coding=cp1251
import win32security, win32net, win32file, win32api, win32gui
import win32netcon, ntsecuritycon,win32con
import os, sys, string
import utils
from utils import process

def CreateUser(userName, params={}):
    # Create user data in information level 1 (PyUSER_INFO_1) format.
    userData={
      'name':userName,
      'password':'1',
      'priv':win32netcon.USER_PRIV_USER,
      'flags':win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_SCRIPT | win32netcon.UF_DONT_EXPIRE_PASSWD
     # string/PyUnicode home_dir 
     # string/PyUnicode comment 
    }
    # update params
    userData.update(params)
 
    # Create the user
    win32net.NetUserAdd(None, 1, userData)
    win32net.NetLocalGroupAddMembers(None, 'Администраторы', 3, [{'domainandname':userName}])

def GetUsersList(filterFunc=None):
    ret=[]
    flResume=1
    while flResume:
        lst,cnt,flResume=win32net.NetUserEnum(None, 0)
        ret+=map(lambda x:x['name'],lst)
    return filter(filterFunc,ret)

def DeleteUser(userName):
    win32net.NetUserDel(None, userName)

def RunAs(userName, Path,Params=None):
    # by default all users have pass=1
    passw='1'
    sCmd='runas /profile /env /user:%s /savecred "\"%s\" %s"'%(userName,Path, reduce(lambda ret,x:ret+'\"%s\" '%x,tuple(Params or []),''))
    process.ExecCommandLine(sCmd)
    time.sleep(0.2)
    wndPass=win32gui.GetForegroundWindow()
    if win32gui.GetClassName(wndPass)=='ConsoleWindowClass':        
        win32api.keybd_event(ord(passw),0)
        win32api.keybd_event(win32con.VK_RETURN,0)

#RunAs(us,r'C:\WINDOWS\system32\dllcache\iexplore.exe')
