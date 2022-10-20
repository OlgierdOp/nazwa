import random

a = [random.randint(1,60)for _ in range(1, 15) ]
b = [random.randint(5,100)for _ in range(1, 20) ]
print(a, b)
c = []
for element in b:
    if element in a:
        c.append(element)


print(c)
