
masa = int(input("Podaj mase: "))
wzrost = int(input("Podaj wzrost w cm: ")) / 100

BMI = masa / (wzrost**2)

print(f'Twoje BMI to: {BMI:.2f}')