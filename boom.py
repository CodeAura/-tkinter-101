import tkinter as tk
import time

Window = tk.Tk()

colors = ["green", "yellow", "orange", "red", "black"] 

Height = 50
Size = 100
x = 0

def changer():
    global x, Height, Size
    Height += 50
    Size += 50
    print(5-x)
    Window.config(bg=colors[x])
    Window.geometry(str(Height) + "x" + str(Size))
    x += 1
     
Window.title("Made by CodeAura")
Window.config(bg="White")
Window.geometry("50x50")
print(6)
for y in range(1, 6):
    Window.after(2000*y, changer)
def explode():
    time.sleep(1)
    print("Bomb has been destroyed")
    Window.destroy()
Window.after(12000, explode)

Window.mainloop()