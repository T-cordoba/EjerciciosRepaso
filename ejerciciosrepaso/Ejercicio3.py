## Crear un programa que genere una lista de números aleatorios y los imprima en pantalla


def random_list (n):
    count = 0
    list = []
    while count < n:
        random_numer = randint (1,99)
        list.append (random_numer)
        count = count + 1