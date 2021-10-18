"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
# Cazul particular in care avem ultima litera din alfabet 'z' o sa returneze 'a'
def increment_asciinr(initial_string):
    initial_list = []
    for i in initial_string:
        char_ascii = ord(i) + 1
        if i == 'z':
            initial_list.append('a')
        else:
            initial_list.append(chr(char_ascii))
    return ''.join(initial_list)

# print(increment_asciinr('abcdz'))
