zadany_text = "ala ma kota"

zliczenia = {}

for znak in zadany_text:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1
print(zliczenia)