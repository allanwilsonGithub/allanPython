try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

def parabola(x):
    y = x * x
    return y

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)

for x in range (-100,100):
    y = parabola(x)
    print(y)

mainWindow.mainloop()