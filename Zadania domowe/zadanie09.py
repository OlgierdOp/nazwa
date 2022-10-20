import random
x = 0
while True:
    num = input("Podaj liczbe: ")
    if num == "exit": break
    else :
        x+=1

        i = random.randint(0, 10)
        print(i)

        if int(num) == i:
            print("Zgadłeś!")
        elif int(num) <=i:
            print("Too low")
        elif int(num) >=i:
            print("Too high")

print("Zagrałeś", x ,"razy")