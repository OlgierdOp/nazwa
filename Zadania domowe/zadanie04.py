liczba = int(input("Podaj liczbe: "))

x=1


while True:
    reszta = liczba % x
    zmienna = liczba / x
    x+=1
    if reszta == 0:
        print(zmienna)
    if x > liczba : break