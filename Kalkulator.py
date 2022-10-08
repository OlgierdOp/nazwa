first_Num = float(input("Podaj wierszą liczbe: "))
second_Num = float(input("Podaj drugą liczbe: "))
operator = str(input("Podaj operator: "))



if operator == "+":
    wynik = first_Num + second_Num
    print("Wynik: ",wynik)
elif operator == "-":
    wynik = first_Num - second_Num
    print("Wynik: ",wynik)
elif operator == "*":
    wynik = first_Num * second_Num
    print("Wynik: ",wynik)
elif operator == "/":
  if second_Num == 0:
    print("Nie dziel przez 0")
    wynik = first_Num / second_Num
    print("Wynik: ",wynik)
elif operator == "**":
    wynik = first_Num ** second_Num
    print("Wynik: ",wynik)
    