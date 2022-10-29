def mul_of(a: list)-> int:
    result = 1
    for i in a:
        result = result * i
    return result

print(mul_of([3,4,5,6,7,73,2]))