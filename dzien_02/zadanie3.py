x = 5
y = 5

while True:
    polecenie = input("Wykonaj ruch wasd: ")
    if polecenie == "w":
        y+=1
    if polecenie == "s":
        y-=1
    if polecenie == "a":
        x-=1
    if polecenie == "d":
        x+=1
    if x < 1 or x > 10:
        print("Wypadłeś poza plansze")
        break
    if y < 1 or y > 10:
        print("Wypadłeś poza plansze")
        break
    print("Pozycja x:", x, "Pozycja y: ", y)





