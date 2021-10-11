"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""

x = int(input())

is_palindrom = True

#transform the int into a list using list comprehension
num_list = [int(i) for i in str(x)]

for n in range(int(len(num_list) / 2)):
    if num_list[n] != num_list[len(num_list) - n - 1]:
        is_palindrom = False

if is_palindrom:
    print(True)
else:
    print(False)