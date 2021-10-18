"""
    Ex. 10: Decoratorul de mai jos printeaza 'cmi' inainte de apelul oricarei
    functii pe care o decoreaza.

    Folosindu-va de kwargs, printati si valoarea lui y dupa ce printati cmi,
    in decorator.

"""


def dec(func):
    def wrapper(**kwargs):
        print('cmi')
        # your code goes here
        n = 1
        for value in kwargs.values():
            if n == 2:
                print(value)
                break
            n += 1
        func (**kwargs)

    return wrapper


@dec
def f(x, y):
    print(x)


f(x=1, y=2)

