import requests


def habilidades(poke):
    print(f"{pokemon} abilities:")
    for i in poke['abilities']:
        print(i['ability']['name'])

def tipo(poke):
    for i in poke['types']:
        type = i['type']
    print(f"Type:{type.get('name')}")

def getpokemoninfo(inp):
    api = f'https://pokeapi.co/api/v2/pokemon/{inp}'
    res = requests.get(api)
    poke = res.json()
    return poke