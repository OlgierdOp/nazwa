def unique(lista: list) -> list:
    lista = set(lista)
    lista1 = []
    for element in set(lista):
        lista1.append(element)
    return lista1

print(unique([1,2,3,4,4,5,6,6,7,]))

def unique2(l):
    x = []
    for el in l:
        if el not in x:
            x.append(el)
    return x

print(unique2([1,2,3,4,4,5,6,6,7,]))