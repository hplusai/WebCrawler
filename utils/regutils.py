import _winreg
import traceback

class RegKey:
    Key=None
    hRootKey=None
    hKey=None
    SubKey=None
    def __init__(self,Key):
        try:
            self.Key=Key
            self.hRootKey=eval('_winreg.%s'%Key[:Key.find('\\')].upper())
            SubKey=Key[Key.find('\\')+1:]
        except:
            Log('Can not read registry key %s'%Key)
            print traceback.format_exc()
            #raise 'Can not read registry key %s'%Key
        self.hKey=_winreg.OpenKey(self.hRootKey,SubKey)
        
    def GetValues(self,flUseUpperCase=0):
        if not self.hKey:
            return None
        flErr=0
        ind=0
        ret={}
        while not flErr:
            try:
                Name,Value,Type=_winreg.EnumValue(self.hKey,ind)
                if flUseUpperCase:
                    Name=Name.upper()
                ret[Name]=Value
            except:
                flErr=1
            ind+=1
        return ret