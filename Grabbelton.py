import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Cars")
window.geometry("1000x1000")
window.configure(bg="gray")

Cars = ["Porsche GT3-RS", "Audi RS6 ABT", "Nissan Silvia S15", "Lamborgini SVJ", "Jeep Trackhawk", "Mazda RX-7", "Mazda Miata", "Koenigsegg Agera R", "Koenigsegg Jesko"]

Randomizer = random.randint(0, 9)

def cars():
    Frame = tk.Label(
        window,
        random.shuffle(Cars),
        text= "Gefeliciteerd, je hebt een " + Cars[Randomizer] + " gegrabbeld!",
        font = ('Calibri', 40, 'bold'),
        fg="Black"
    )
    messagebox.showwarning("Car", "Gefeliciteerd, je hebt een " + Cars[Randomizer] + " gegrabbeld!"),
    Frame.pack()
    

button = tk.Button(
    window, 
    text="Grabbelen", 
    font = ('Calibri', 40, 'bold'),
    fg="white",
    bg="Black",
    command= cars 
)
button.pack()



window.mainloop()