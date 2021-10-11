"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""

x = input()
y = []

for n in range(len(x)):
    if(n % 2 == 0):
        z= x[n].upper()
        y.append(z)
    else:
        y.append(x[n])

result = ''.join(y)
print(result)