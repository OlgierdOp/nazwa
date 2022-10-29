import random
password = ''
pool = "abcdefghijklmnopqrstuvwxyz@#$!%^&*()"
lenght = int(input("Podaj dlugość hałsa: "))
x=0
while x < lenght:
    x+=1
    losowanie = random.randint(0, len(pool))
    znak = pool[losowanie]
    password = password + znak


print(password)



