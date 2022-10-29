def even(lista: list) -> list:
    result = []
    for element in lista:
        if element % 2 == 0:
            result.append(element)
    return result

print(even([1,2,3,4,5,6,7,7,8,8,9,9,4,3,3,2,3,4,6,6,7,8]))
