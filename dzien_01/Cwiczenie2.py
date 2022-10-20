miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")

dystans = int(input(f"Oległośc pomiędzy {miasto_a} - {miasto_b}: "))

cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100km: "))
koszt = dystans * cena_paliwa / spalanie

print("Koszt paliwa to: ", koszt)
