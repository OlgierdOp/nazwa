oferta= {"marchew" : 3.00, "ziemniaki" : 5.00, "jabłka" : 2.00}


for elements in oferta:
    print(elements, ": ", oferta[elements], "PLN za kg")

jedzenie = input("Co chcesz kupić: ")
waga = int(input("Ile chcesz kupić: "))

print("Należy się ", waga * oferta[jedzenie],"PLN" )



