def no_duplicates():
    a_list = [2, 2, 2, 3, 4, 4, 6, 6, 7, 7, 8, 8, 8, 45, 45, 4, 4, 4, 3, 3, 4, 5, 5, 5, 5, 5, ]
    b_list = []
    for element in a_list:
        if element not in b_list:
            b_list.append(element)


    return (b_list)


print(no_duplicates())
