## Crear una función que invierta el orden de los elementos en una lista dada.

l=[1,2,3,4,9,6]

def inv_list(l):
    result=[]
    for i in range((len(l)-1),-1,-1):
        result.append(l[i])
    return result

result=inv_list(l)
print(result)