## Crear un programa que calcule la suma de los números en una lista dada

l=[1,2,3,4,5,6]
def sum_list(l):
    result=0
    for i in range(len(l)):
        result+=l[i]
    return result

result=sum_list(l)
print(f"La suma de los números en la lista {l} es {result}")