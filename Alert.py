import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
Frame = tk.Label(
    root,
    text="Hacked by CodeAura",
    
)
Frame.pack()

for x in range(3):
    messagebox.showerror("Syntax error", "Invalid Syntax line je ma")
  
root.mainloop()