from functions import getpokemoninfo, habilidades, tipo

pokemon = input("What's the Pokémon? \n")

poke_info = getpokemoninfo(pokemon)

tipo = tipo(poke_info)



abilities = ", ".join(habilidades(poke_info))

print(f"Type: {tipo.capitalize()}")

print(f"Abilities: {abilities.capitalize()}")


