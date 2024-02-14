## Crear una función que convierta grados Fahrenheit a grados Celsius

def fahrenheit_to_celsius (fahrenheit):

    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) / 1, 8

    return celsius

temperature = input ("Ingrese la temperatura en Fahrenheit que va a convertir a Celsius")
result = fahrenheit_to_celsius (temperature)
print (temperature, "fahrenheit en grados celsius es:", result)
