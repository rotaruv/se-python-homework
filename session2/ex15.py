"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input()

count = 0

def isChar(letter):
    return letter.lower() in 'aeiou'

for n in x:
    if isChar(n):
        count+=1

print(count)