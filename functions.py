import requests
from PIL import Image
from io import BytesIO

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


def get_image(a):
    url = a['sprites']['front_default']
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()



