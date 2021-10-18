"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""

def change_output_decorator(func):
    def wrapper():    
        return func().upper()
    return wrapper

# decoarate me
@change_output_decorator
def f():
    return 'cmi'

print(f())