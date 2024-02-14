## Escribir un programa que determine si un número dado es par o impar.

def even_or_odd(n):
    if n%2 == 0:
        return f"El numero {n} es par"
    else:
        return f"El numero {n} es impar"

num=int(input("Ingrese un número "))
result=even_or_odd(num)

print(result)