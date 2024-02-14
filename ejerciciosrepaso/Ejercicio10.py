## Escribir una función que calcule el factorial de un número dado.

def factorial(n):
    result=0
    for i in range(n,0,-1):
        result=result*i
    return result

