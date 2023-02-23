import random 

def ordenar_lista(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = random.choice(lista)

    menores,iguales,mayores = [],[],[]

    for item in lista:
        if item < pivot:
            menores.append(item)
        elif item == pivot:
            iguales.append(item)
        else:
            mayores.append(item)
    
    return ordenar_lista(menores) + iguales +ordenar_lista(mayores)
