"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""
import random
import string 

def add_text_in_file_decorator(func):
    def wrapper(*args):
        func(args[0])
        # folosim append --> 'a'
        with open('output17.data', 'a') as f:
            f.write(func(args[0]))
            f.writelines('\n')

    return wrapper

@add_text_in_file_decorator
def f(x):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(x))

# f(20)