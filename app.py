from functions import getpokemoninfo, habilidades, tipo
from tkinter import *

ws = Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

def printValue():
    global pokemon, tipo
    pokemon = player_name.get()
    poke_info = getpokemoninfo(pokemon)
    print(poke_info)
    tipo = tipo(poke_info)
    abilities = ", ".join(habilidades(poke_info))
    print(f"Type: {tipo.capitalize()}")
    print(f"Abilities: {abilities.capitalize()}")


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    text="Register Player", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()







