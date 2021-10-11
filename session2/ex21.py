"""
    Veti primi stringuri de la tastatura, pana cand primiti stringul 'exit'.
    Va trebui sa printati o lista cu stringurile primite fara ultimul caracter
    al fiecarui string.

    Observatii:
        - lungimea stringurilor va fi intotdeauan cel putin 1

    exemplu:
        Veti primi: 'cmi', 'center', 'for', 'machines'
        Veti printa: ['cm', 'cente', 'fo', 'machine']
"""

x = input()
y = []

while x != 'exit':
    x = x[:-1]
    y.append(x)
    x = input()

print(y)
