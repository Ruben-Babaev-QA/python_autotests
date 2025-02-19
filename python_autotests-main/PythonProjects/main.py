import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN }

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post( url = f'{URL}/pokemons',headers = HEADER,json = body_create )

POKEMON_ID =response_create.json()['id'] #присваиваем переменной id созданного покемона
print ('айди покемона', POKEMON_ID)

body_rename = {                      # запихиваем в body айди созданного покемона
    "pokemon_id": POKEMON_ID,        
    "name": "СуперШурик",
    "photo_id": 2
}


response_rename = requests.put( url = f'{URL}/pokemons',headers = HEADER,json = body_rename )
print (response_rename.text)

body_add ={
    "pokemon_id": POKEMON_ID    
}

response_add = requests.post( url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_add )
print(response_add.text)

'''
response_rename = requests.put( url = f'{URL}/pokemons',headers = HEADER,json = body_create )

print (response_create.text)
print (response_create.status_code)
message =response_create.json()['message']
print (message)
response_rename =requests.put( url = f'{URL}/pokemons',headers = HEADER,json = body_create )
'''



'''response = requests.post(url = f'{URL}/trainers/reg',headers = HEADER,json = body_registration  )
print (response.text)
print (response.status_code)'''




