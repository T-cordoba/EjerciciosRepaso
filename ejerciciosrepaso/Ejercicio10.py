## Escribir una función que calcule el factorial de un número dado.

def factorial(n):
    for i in range(1,n):
        n=n*i
    return n

n=int(input("Ingrese el número al que va a calcular el factorial "))
result=factorial(n)

print(f"El factorial de {n} es {result}")