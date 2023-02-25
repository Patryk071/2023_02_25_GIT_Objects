liczby = [1, 2, 3, 4, 5, 6, 7]

#1 sposób
liczbyParzyste1 = []

for liczba in liczby:
    if (liczba % 2) == 0:
        liczbyParzyste1.append(liczba)

print(liczbyParzyste1)

#sposób 2
liczbyParzyste2 = [element
                   for element in liczby
                   if (element % 2) == 0]

print(liczbyParzyste2)


#ZADANIE - podnieść do potęgi 2 każdy z elementów listy
liczbyDoKwadratu = [element**2
                    for element in liczby]

print(liczbyDoKwadratu)