def perfect(a: int) -> bool:
    lista = []
    for i in range(1, a):
        if a % i == 0:
            lista.append(i)
            x = sum(lista)
            print(lista, x)
        else:
            continue
    if x == a:
        return True
    else:
        return False



print(perfect(8128))
