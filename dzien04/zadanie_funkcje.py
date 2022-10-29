def zliczanie(napis: str) -> int:
    i=0
    czy_zliczac = False

    for znak in napis:
        if znak == "<" or "[":
          czy_zliczac = True
          continue
        elif znak == ">" or "]":
            czy_zliczac = False

        if czy_zliczac: # is True
            i+=1
    return i

print(zliczanie("Ala ma <kota> [kot] ma ale"))

