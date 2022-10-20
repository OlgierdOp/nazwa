while True:
    a = input("Rock Paper Sissors: ")
    b = input("Rock Paper Sissors: ")

    c = "Gracz a wygrywa!"
    d = "Gracz b wygrywa!"
    e = "Remis"

    if a == "Rock" and b == "Rock":
        print(e)
    elif a == "Rock" and b == "Paper":
        print(d)
    elif a == "Rock" and b == "Sissors":
        print(c)
    elif a == "Paper" and b == "Rock":
        print(c)
    elif a == "Paper" and b == "Sissors":
        print(d)
    elif a == "Paper" and b == "Paper":
        print(e)
    elif a == "Sissors" and b == "Rock":
        print(d)
    elif a == "Sissors" and b == "Sissors":
        print(e)
    elif a == "Sissors" and b == "Paper":
        print(d)

    else:
        print("Nie wiem co to!")
