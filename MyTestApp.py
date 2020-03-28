__author__      = 'Victor Santiago'
__copyright__   = 'Copyright (C) 2014, Victor Santiago'
__credits__     = ['Victor Santiago']
__license__     = 'The MIT License (MIT)'
__version__     = '1.0'
__maintainer__  = 'Victor Santiago'
__email__       = 'vsantiago@vs113dev.com'
__status__      = 'Beta'

_AppName_ = 'MyTestApp'

import Tkinter as tk
import tkMessageBox as messagebox
from PIL import ImageTk, Image, ImageOps
import tkFont as font
from Modules.MessageBox import *
import ttk, os, webbrowser, urllib2, ctypes, win32api, threading, cgi

class Main:
    def __init__(self, parent):
        def CheckUpdates():
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                data = urllib2.urlopen('https://drive.google.com/uc?id=0B165Q_pWKZAeUlFGUElvcE40Yzg').read()
                
                # -- Local Version File
                #f = open('version.txt','r')
                #data = f.read()
                #f.close()
                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update','Update Available!')
                    mb = MessageBox(None,_AppName_+' '+str(__version__)+' needs to update to version '+str(data),'Update',flags.MB_YESNO | flags.MB_ICONQUESTION)
                    if mb == 'Yes':
                        # -- Replace the url for your file online with the one below.
                        webbrowser.open_new_tab('https://drive.google.com/uc?id=0B165Q_pWKZAed09HMjFmTTNpQXM')
                        parent.destroy()
                    elif mb == 'No':
                        pass
                else:
                    messagebox.showinfo('Software Update','No Updates are Available.')
            except Exception as e:
                messagebox.showinfo('Software Update','Unable to Check for Update, Error:' + str(e))

        def AboutMe():
            CallDisplayAboutMe = DisplayAboutMe(parent)

        def runBinary():
            ctypes.windll.Shell32.ShellExecuteA(0,'open','binaries\\TestBinary.exe',None,None,10)

        def RUNCMD():
            ctypes.windll.Shell32.ShellExecuteA(0,'open','cmd.exe','/k ipconfig',None,10)

        def UpdateUsingManager():
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                data = urllib2.urlopen('https://drive.google.com/uc?id=0B165Q_pWKZAeUlFGUElvcE40Yzg').read()
                
                # -- Local Version File
                #f = open('version.txt','r')
                #data = f.read()
                #f.close()
                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update','Update Available!')
                    mb = MessageBox(None,_AppName_+' '+str(__version__)+' needs to update to version '+str(data),'Update',flags.MB_YESNO | flags.MB_ICONQUESTION)
                    if mb == 'Yes':
                        CallUpdateManager = UpdateManager(parent) #################################################################################################################################################
                    elif mb == 'No':
                        pass
                else:
                    messagebox.showinfo('Software Update','No Updates are Available.')
            except Exception as e:
                print 'The Error is here!'
                messagebox.showinfo('Software Update','Unable to Check for Update, Error:' + str(e))

        def StartApp():
            menubar = tk.Menu(parent)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label='Exit', command=parent.destroy)
            menubar.add_cascade(label='File', menu=filemenu)
            helpmenu = tk.Menu(menubar, tearoff=0)
            helpmenu.add_command(label='About', command=AboutMe)
            menubar.add_cascade(label='Help', menu=helpmenu)
            parent.config(menu=menubar)

            ButtonsFrame = tk.Frame(parent, bg='#FFFFFF')
            ButtonsFrame.pack(side='top', fill='x')

            self._exit = ImageTk.PhotoImage(Image.open('images/exit.png'))

            exitButton = ttk.Button(ButtonsFrame, image=self._exit, command=parent.destroy)
            exitButton.pack(side=tk.LEFT, padx=1, pady=1)

            button1 = ttk.Button(parent, text='Check for Updates', command=CheckUpdates)
            button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            button2 = ttk.Button(parent, text='Execute', command=runBinary)
            button2.place(x=20, y=60)

            button3 = ttk.Button(parent, text='Run CMD', command=RUNCMD)
            button3.place(x=20, y=100)

            button4 = ttk.Button(parent, text='UpdateManager', command=UpdateUsingManager)
            button4.place(x=-200, relx=1.0, y=60)

# Fix this part here ####################################################################################################################################################################################
        if os.path.isfile(r'version.txt'):
            f=open(r'version.txt','r')
            GetVersionFromFile = f.read().replace('\n','').strip()
            if float(GetVersionFromFile) > float(__version__):
                f.close()
                try:
                    mb = MessageBox(None,_AppName_+' '+str(__version__)+' needs to update to version '+str(GetVersionFromFile),'Update',flags.MB_YESNO | flags.MB_ICONQUESTION)
                    if mb == 'Yes':
                        win32api.ShellExecute(0,'open',r'updates\MyTestApp.msi',None,None,10)
                        parent.destroy()
                    elif mb == 'No':
                        StartApp()
                except:
                    messagebox.showerror('Error', 'Software Update Failed.  An error occurred updating '+_AppName_+' '+str(__version__)+'. Please contact your system administrator.')
                    parent.destroy()
            else:
                StartApp()
        else:
            messagebox.showerror('Error', 'Version file is missing.')
            parent.destroy()
#########################################################################################################################################################################################################

class UpdateManager(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        
        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350; h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('Update Manager')
        self.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')

        image = Image.open('images/updatemanager.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()

        def StartUpdateManager():
            pass
##            try:
##                f = open(self.tempdir+'/'+self.appname,'wb')
##                while True:
##                    self.newdata = self.data.read(self.chunk)
##                    if self.newdata:
##                        f.write(self.newdata)
##                        self.downloadeddata += self.newdata
##                        self.progressbar['value'] = len(self.downloadeddata)
##                    else:
##                        break
##            except Exception as e:
##                messagebox.showerror('Error',str(e))
##                self.destroy()
##            else:
##                f.close()
##                self.button1.config(text='Install', state=tk.NORMAL)

        def InstallUpdate():
            win32api.ShellExecute(0,'open',self.tempdir+'/'+self.appname,None,None,10)
            parent.destroy()

        params = cgi.parse_header(self.data.headers.get('Content-Disposition', ''))
        filename = params[-1].get('filename')
        self.appname = filename
        self.tempdir = os.environ.get('temp')
        self.chunk = 1048576
        
        try:
            # -- Online updated program
            # -- Replace the url for your file online with the one below.
            #self.data = urllib2.urlopen('http://yourdomaindotcom/MyTestApp/'+self.appname)

            # For my Google Drive. This is because Google Drive won't let me see the file name just a string.
            temp_data = urllib2.urlopen('https://drive.google.com/uc?id=0B165Q_pWKZAed09HMjFmTTNpQXM')
            self.data = temp_data.read()
        except Exception as e:
            messagebox.showerror('Error',str(e))
            self.destroy()
        else:
            self.downloadeddata = ''
            self.progressbar = ttk.Progressbar(self,
                                   orient='horizontal',
                                   length=200,
                                   mode='determinate',
                                   value=0,
                                   #maximum=self.data.info().getheader('Content-Length').strip())len(data.read())
                                   maximum=len(self.data))
            self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.button1 = ttk.Button(self, text='Wait!', state=tk.DISABLED, command=InstallUpdate)
            self.button1.place(x=-83, relx=1.0, y=-33, rely=1.0)
            if os.path.isfile(self.tempdir+'/'+self.appname):
                os.remove(self.tempdir+'/'+self.appname)
            else:
                pass
        self.t1 = threading.Thread(target=StartUpdateManager)
        self.t1.start()

class DisplayAboutMe(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        
        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 285; h = 273
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('About')
        self.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')

        self.image = Image.open('images/vs.png')
        self.size = (100, 100)
        self.thumb = ImageOps.fit(self.image, self.size, Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.thumb)
        logoLabel = tk.Label(self, image=self.photo); logoLabel.pack(side=tk.TOP, pady=10)

        f1 = tk.Frame(self); f1.pack()
        f2 = tk.Frame(self); f2.pack(pady=10)
        f3 = tk.Frame(f2); f3.pack()

        def CallHyperLink(EventArgs):
            webbrowser.open_new_tab('https://plus.google.com/102816536178598532938')

        tk.Label(f1, text=_AppName_+' '+str(__version__)).pack()
        tk.Label(f1, text='Copyright (C) 2014 Victor Santiago').pack()
        tk.Label(f1, text='All rights reserved').pack()

        f = font.Font(size=10, slant='italic', underline=True)
        label1 = tk.Label(f3, text='vsantiago113', font = f, cursor='hand2')
        label1['foreground'] = 'blue'
        label1.pack(side=tk.LEFT)
        label1.bind('<Button-1>', CallHyperLink)
        ttk.Button(self, text='OK', command=self.destroy).pack(pady=5)
         
def main():
    root = tk.Tk()
    root.title(_AppName_+' '+str(__version__))
    w=650; h=400
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
    root.resizable(width=False, height=False)
    root.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')
    win = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
