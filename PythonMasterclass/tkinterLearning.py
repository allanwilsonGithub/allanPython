try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+10+200')


mainWindow.mainloop()