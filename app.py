import requests
from teste import habilidades, tipo, getpokemoninfo

import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget
getpokemoninfo('pikachu')

def get_input():
    inp = inputtxt.get(1.0, "end-1c")
    return inp


# TextBox Creation
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Print",
						command = get_input)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()

