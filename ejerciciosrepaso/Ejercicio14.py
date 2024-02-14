## Escribir una función que calcule la media aritmética de una lista de números.

l=[5,1,3,7,2,5]

def arith_average(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s/len(l)

result=arith_average(l)

print(result)