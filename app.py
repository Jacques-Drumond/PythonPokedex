from functions import getpokemoninfo, habilidades, tipo, get_image
from tkinter import *

ws = Tk()
ws.title("Pokédex")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

def printValue():
    global pokemon, tipo
    pokemon = player_name.get()
    poke_info = getpokemoninfo(pokemon)
    tipo = tipo(poke_info)
    abilities = ", ".join(habilidades(poke_info))
    print(f"Pokémon: {pokemon.capitalize()}")
    print(f"Type: {tipo.capitalize()}")
    print(f"Abilities: {abilities.capitalize()}")
    get_image(poke_info)


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    text="Submit", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()







