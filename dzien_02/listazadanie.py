dane = []

while True:
    d = input("Podaj liczbe lub k by zakonczyc: ")
    if d == "k":
        break
    dane.append(int(d))

print(f"Srednia =", sum(dane) / len(dane))



