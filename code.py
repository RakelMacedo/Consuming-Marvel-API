import hashlib
import requests

from decouple import config
from rich import print
from rich.console import Console

from save_to_csv import save_to_csv

heros = []
console = Console()


def compute_md5_hash(my_string):
    '''
    Convert string to md5 hash
    '''
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def make_authorization():
    '''
    Generate authorization tokens
    '''
    publicKey = config('PUBLIC_KEY')
    privateKey = config('PRIVATE_KEY')
    ts = 1
    md5_hash = compute_md5_hash(f'{ts}{privateKey}{publicKey}')
    query_params = f'?ts={ts}&apikey={publicKey}&hash={md5_hash}'
    return query_params


def main(url):
    url += make_authorization()
    with requests.Session() as session:
        response = session.get(url)
        print(response)
        characters = response.json()['data']['results']

        for character in characters:
            name = str(character['name'])
            description = str(character['description']) 
            
            hero = {
                'name' : name,
                'description' : description,
            }

            heros.append(hero)
            


if __name__ == '__main__':
    endpoint = 'http://gateway.marvel.com/v1/public/characters'
    main(endpoint)

    save_to_csv(heros)