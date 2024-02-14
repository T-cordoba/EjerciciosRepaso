## Crear un programa que genere una matriz de números y la imprima en pantalla

import random

m=[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]

def gen_matrix(m):
    for i in range(5):
        for j in range(5):
            m[i][j]=random.randint(0,20)
    return m

result=gen_matrix(m)
print(f"{result[0]}\n{result[1]}\n{result[2]}")