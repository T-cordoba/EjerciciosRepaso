## Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

num_1 = input ("Por favor ingrese un número: ")
num_2 = input ("Por favor ingrese otro número: ")
number = float (num_1)
number2 = float (num_2)

def add (num_1, num_2):
    return num_1 + num_2

def substract (num_1, num_2):
    return num_1 - num_2

def multiplication (num_1, num_2):
    return num_1 * num_2

def division (num_1, num_2):
    return num_1 / num_2

sum = add  (number, number2)
sub =  substract  (number, number2)
mul = multiplication  (number, number2)
div = division  (number, number2)

print ("La suma de los números que usted dió es:", sum)
print ("La resta de los números que usted dió es:", sub)
print ("La multiplicación de los números que usted dió es:", mul)
print ("La división de los números que usted dió es:", div)