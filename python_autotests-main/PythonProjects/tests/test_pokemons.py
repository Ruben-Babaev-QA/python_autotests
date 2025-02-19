import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' # для этих двух тестов нужен только URL


def  test_status_code():
    response = requests.get(url = f'{URL}/trainers' )
    assert response.status_code == 200

def   test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers',params ={'trainer_id':'17050'} )
    assert response_get.json()["data"][0]["trainer_name"]=='Defis'


'''@pytest.mark.parametrize('key,value',[('name','Бульбазавр'),('trainer_id',TRAINER_ID ),('id','166775')])    
def test_parametrize(key,value):
    response_paramertize = requests.get(url = f'{URL}/pokemons',params ={'trainer_id':TRAINER_ID} )
    assert response_paramertize.json()["data"][0][key] == value'''


