from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from os import path
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filePath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
fileBasename = path.abspath(filePath).split('.') 
fileName   = fileBasename[0]
fileEnding = '.' + fileBasename[1]


#For testing    
if __name__ == "__main__":
    print("fileName",fileName)
    print("fileEnding",fileEnding)