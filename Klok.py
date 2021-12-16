# importing whole module
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Klok')
 
def tijd():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, tijd)
 
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')

lbl.pack(anchor = 'center')
tijd()
 
mainloop()