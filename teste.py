import requests


def habilidades(poke):
    print(f"Habilidades de {pokemon}")
    for i in poke['abilities']:
        print(i['ability']['name'])

def tipo(poke):
    for i in poke['types']:
        type = i['type']
    print(f"Type:{type.get('name')}")

def main():
    global pokemon
    pokemon = str(input('Qual o Pokémon?'))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    habilidades(poke)
    tipo(poke)

if __name__ == '__main__':
    main()
    
    