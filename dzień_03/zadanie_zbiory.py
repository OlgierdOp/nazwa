b = set(range(0,100,2))
i = 0
a = set()
x = int(input("Ile liczb chesz wprowadzić: "))

while i < x:
    liczba = int(input("Podaj liczbe: "))
    a.add(liczba)
    i+=1
print("Unikalnych liczb parzystych jest: ", len(a & b))


