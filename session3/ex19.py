"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""

import random
import string
import json


def create_dict(my_string):
    my_dict = {}
    letters = string.ascii_letters

    for _ in range(0, 4):
        random_key = random.randint(0, 10)
        # check if the generated key exists already in dict --> generate a new one in that case
        while random_key in my_dict:
            random_key = random.randint(0, 10)
        random_value = ''.join(random.choice(letters) for i in range(random.randint(3, 6)))
        my_dict[random_key] = random_value

    with open(f'{my_string}.json', 'w') as f:
        # dict to string using dumps method
        f.write(json.dumps(my_dict))


create_dict('test')