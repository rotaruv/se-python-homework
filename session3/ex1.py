"""
    Ex. 1: Functia de mai jos returneaza X la puterea Y.
    Modificati aceasta functie incat sa intoarca X la puterea Y la puterea Z.
"""


def power(x, y, z):
    return x ** y ** z

# x ** y ** z sau (x ** y) ** z
# (2 ** 3) ** 2 = 64
# 2 ** 3 ** 2 = 512
print(power(2, 3, 2))
