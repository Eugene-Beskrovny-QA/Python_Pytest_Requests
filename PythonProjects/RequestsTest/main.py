import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3f7b301a856cfb93b65dfe673040a221'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_changes = {
    "pokemon_id": "166815",
    "name": "Bloodr",
    "photo_id": -1
}
body_inpokeball = {
    "pokemon_id": "166815"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_changes = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changes)
print(response_changes.text)'''

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball)
print(response_inpokeball.text)