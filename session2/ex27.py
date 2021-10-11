"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""

import random

x = int(input())

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random_string = ''

for n in range(x):
    character = random.choice(alphabet_list)
    random_string += character

print(random_string)