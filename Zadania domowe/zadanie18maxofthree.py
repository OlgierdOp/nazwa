def max_of_two(a, b):
    if a < b:
        return b
    else:
        return a


def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))


print(max_of_three(300, 30, 2))
