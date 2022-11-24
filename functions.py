import requests


def habilidades(poke):
    ab = []
    for i in poke['abilities']:
        ab.append(i['ability']['name'])
    return ab

def tipo(poke):
    for i in poke['types']:
        tipo = i['type']['name']
    return tipo


def getpokemoninfo(pokemon):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    return poke