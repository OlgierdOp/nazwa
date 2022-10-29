def splaszczanie():
        a = [1,2,3,[4,5,[6]], 7]
        b = []
        c = []
        d = []
        for element in a:
            if type(element) is not list:
                b.append(element)




print(splaszczanie())