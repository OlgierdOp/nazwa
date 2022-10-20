rok = 2022
wiek = int(input("Podaj swoj wiek: "))
liczba = int(input("Podaj jakąś liczbe: "))

ile_lat_do_stu = 100 - wiek

rok_sto_lat = rok + ile_lat_do_stu
i = 0

while i < liczba:
    i+=1
    print("Bedziesz miał 100 lat w roku: ", rok_sto_lat)