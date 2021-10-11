"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""

x = int(input())

sum = 0

for n in range(x + 1):
    sum += n

print(sum)