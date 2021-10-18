"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""

import sys

def add_input_in_file(func):
    def wrapper(*args, **kwargs):
        # salvam o referinta a stdout'ului original
        original_stdout = sys.stdout
        with open('output12.data', 'w') as f:
            # atribuim stdout'ul fisierului in care v'om scri
            sys.stdout = f
            func(args[0])
            # revenim la stdout't original
            sys.stdout = original_stdout
    return wrapper


# decorate me
@add_input_in_file
def f(x):
    print(x)


# f("alabala")