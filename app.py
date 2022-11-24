from functions import getpokemoninfo, habilidades, tipo

pokemon = input("What's the Pokémon? \n")

poke_info = getpokemoninfo(pokemon)

tipo = tipo(poke_info)

ab = habilidades(poke_info)

abilities = ", ".join(ab)

print(f"Type: {tipo.capitalize()}")

print(f"Abilities: {abilities.capitalize()}")


