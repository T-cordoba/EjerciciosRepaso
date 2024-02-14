## Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

def find_number (list):
    splited_list = list.split ("")
    lowest_number = 999999
    highest_number = 0

    for i in splited_list:
        current_number = int(i)
        if current_number < lowest_number:
            lowest_number = int(i)

        if current_number > highest_number:
            highest_number = int(i)

    return ("El número mayor es ", highest_number, " y el número menor es ", lowest_number)

values = input("Ingrese una lista separada por comas")
result = find_number (values)
print (result)