"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""

x = input()

vowels = 'aeiou'
vowels_number = 0
consonants_number = 0

for n in x:
    if n in vowels:
        vowels_number += 1
    else:
        consonants_number += 1

print(f'Vowels number: {vowels_number}')
print(f'Consonants number: {consonants_number}')