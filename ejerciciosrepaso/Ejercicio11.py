##Crear un programa que genere una lista de números pares entre 1 y 100

list = [ ]

x = 1

while x <= 100:
    if x % 2 == 0:
        list.append (x)
    x = x + 1


print ("La lista de los números pares del 1 al 100 es", list)