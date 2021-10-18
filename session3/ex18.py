"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""

def recursive_sum(num_list):
    if len(num_list) == 0:
        return
    elif len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[- 1] + recursive_sum(num_list[:-1])

# result = recursive_sum([])
# print(result)

