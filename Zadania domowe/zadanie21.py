def fratorial(a):
    if a < 0:
        raise ValueError("a musi być większe od 0")
    if a == 0:
        return 1
    return a * fratorial(a - 1)
print(fratorial(994))