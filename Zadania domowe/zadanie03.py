lista1 = [1,2,3,4,5,23,4,1,7,8,4,12,1,4,4,5,23,1]
print(lista1)
lista2 = []
liczba = int(input('Podaj liczbe: '))
for element in lista1:
    if element < liczba:
        lista2.append(element)

print(lista2)