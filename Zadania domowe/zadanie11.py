a = []
c = []

x = 0

while True:
    b = input("Podaj liczbe: ")
    a.append(b)
    c.append(b)
    if b == "stop":
        break
while len(a) == x:
    a.remove("stop")
    c.remove("stop")
    d = [int(b) for b in c and int(b) for b in a]
    if len(d) == 2:
        i = sum(d)
        a.append(i)
        d.clear()
        x+=1



print(a)
print(len(a))

