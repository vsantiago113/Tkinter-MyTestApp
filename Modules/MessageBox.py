__author__      = 'Victor Santiago'
__credits__     = 'Victor Santiago(vs113dev.com)'
__license__     = 'GNU GPL v2.0'
__version__     = '1.0'
__maintainer__  = 'Victor Santiago'
__email__       = 'vsantiago@vs113dev.com'

# http://msdn.microsoft.com/en-us/library/windows/desktop/ms645505%28v=vs.85%29.aspx

from ctypes import windll
from ctypes.wintypes import HWND, LPCSTR, UINT

class flags:
    def __init__(self):
        
        flags = {"MB_ABORTRETRYIGNORE":0x00000002,
                 "MB_CANCELTRYCONTINUE":0x00000006,
                 "MB_HELP":0x00004000,
                 "MB_OK":0x00000000,
                 "MB_OKCANCEL":0x00000001,
                 "MB_RETRYCANCEL":0x00000005,
                 "MB_YESNO":0x00000004,
                 "MB_YESNOCANCEL":0x00000003,
                 "MB_ICONEXCLAMATION":0x00000030,
                 "MB_ICONWARNING":0x00000030,
                 "MB_ICONINFORMATION":0x00000040,
                 "MB_ICONASTERISK":0x00000040,
                 "MB_ICONQUESTION":0x00000020,
                 "MB_ICONSTOP":0x00000010,
                 "MB_ICONERROR":0x00000010,
                 "MB_ICONHAND":0x00000010,
                 "MB_DEFBUTTON1":0x00000000,
                 "MB_DEFBUTTON2":0x00000100,
                 "MB_DEFBUTTON3":0x00000200,
                 "MB_DEFBUTTON4":0x00000300,
                 "MB_APPLMODAL":0x00000000,
                 "MB_SYSTEMMODAL":0x00001000,
                 "MB_TASKMODAL":0x00002000,
                 "MB_DEFAULT_DESKTOP_ONLY":0x00020000,
                 "MB_RIGHT":0x00080000,
                 "MB_RTLREADING":0x00100000,
                 "MB_SETFOREGROUND":0x00010000,
                 "MB_TOPMOST":0x00040000,
                 "MB_SERVICE_NOTIFICATION":0x00200000,
                 }
        
        for key, value in flags.items():
            setattr(self, key, value)

flags = flags()

def MessageBox(HWND, BODY, TITLE, UINT):

    code = {3:"Abort",
            2:"Cancel",
            11:"Continue",
            5:"Ignore",
            7:"No",
            1:"OK",
            4:"Retry",
            10:"Try Again",
            6:"Yes"}
    
    int = windll.User32.MessageBoxA(
        HWND,
        LPCSTR(BODY),
        LPCSTR(TITLE),
        UINT
        )
    
    return code[int]
