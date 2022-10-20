liczba = int(input("Podaj liczbe: "))
reszta_z_dzielenia = liczba % 2



if reszta_z_dzielenia == 0:
    print("liczba jest  parzysta!")
else:
    print("liczba jest nie parzysta!")

    reszta_z_dzielenia = liczba % 4

    print("liczba jest podzielna przez 4!")
    if reszta_z_dzielenia == 0:
        print("liczba jest podzielna przez 4!")
    else:
        print("liczba nie jest podzielna przez 4!")

print(liczba % 4)

