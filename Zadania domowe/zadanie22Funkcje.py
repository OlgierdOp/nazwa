def how_much_upper_or_lower(phrase: str):
    i = 0
    x = 0
    for letter in phrase:
        if letter.isupper():
            i+=1
        elif letter == " ":
            pass
        else:
            x+=1
    return (i,x)

print(how_much_upper_or_lower("Ala ma Kota"))


