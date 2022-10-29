def czy_pierwsza(arg):
    if arg > 1:
        for n in range(2, arg):
            if arg % n == 0:
                return False
        return True
    else:
        return False

print(czy_pierwsza(5))
