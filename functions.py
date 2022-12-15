import requests
from PIL import Image
from io import BytesIO

class Pokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    @classmethod
    def getpokemoninfo(cls, pokemon):
            try:
                api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
                res = requests.get(api)
                poke = res.json()
                return poke
            except:
                print(f"Cound't find {pokemon} in API")

    @classmethod
    def habilidades(cls, dict):
        ab = []
        for i in dict['abilities']:
            ab.append(i['ability']['name'])
        return ab

    @classmethod
    def tipo(cls, dict):
        for i in dict['types']:
            tipo = i['type']['name']
        return tipo

    @classmethod
    def get_image(cls, dict):
        url = dict['sprites']['front_default']
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        yield img.show()

pokemon = input("??")

pokemon_dictionary = Pokemon.getpokemoninfo(pokemon)

print(pokemon_dictionary)

habilities = Pokemon.habilidades(pokemon_dictionary)

type = Pokemon.tipo(pokemon_dictionary)

pokemon_image = Pokemon.get_image(pokemon_dictionary)

next(pokemon_image)