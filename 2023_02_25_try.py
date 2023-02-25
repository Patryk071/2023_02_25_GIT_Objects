
licznik = 0

while True:
    x = input("Podaj liczbę całkowitą: ")

    try:
        x = int(x)
    except ValueError:
        print("Hej, nie podałeś liczby całkowitej.")
        licznik += 1
        if licznik == 2:
            print("2 razy się pomyliłeś, papa")
            break
    else:
        print("Dzięki za prawidłową liczbę")

print(type(x))