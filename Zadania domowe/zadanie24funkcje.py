def prime(n: int) -> bool:
    for i in range(2, (n - 1)):
        if n <= 1:
            return "Musi być większa niż 1"
        if n % 2 == 1:
            return True
        if n == 2:
            return True
        else:
            return False


print(prime(1))
