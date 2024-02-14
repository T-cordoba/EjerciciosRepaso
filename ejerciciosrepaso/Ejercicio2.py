## Escribir una función que calcule el área de un círculo dado su radio.

import math

def circle_area (r):
    return math.pi*r**2

ask_radius = int(input("Ingrese el radio del circulo "))
area_result = circle_area(ask_radius)

print(f"El area del circulo es de {area_result} unidades cuadradas")