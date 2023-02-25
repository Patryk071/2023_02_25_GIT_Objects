#Lista z liczbami
liczby = [1, 2, 3, 4, 5, 6, 7]

#1 sposób - wybrać tylko elementy parzyste z listy
liczbyParzyste1 = []

for liczba in liczby:
    if (liczba % 2) == 0:
        liczbyParzyste1.append(liczba)

print(liczbyParzyste1)

#sposób 2 - wybrać tylko elementy parzyste z listy
liczbyParzyste2 = [element
                   for element in liczby
                   if (element % 2) == 0]

print(liczbyParzyste2)


#ZADANIE - podnieść do potęgi 2 każdy z elementów listy
liczbyDoKwadratu = [element**2
                    for element in liczby]

print(liczbyDoKwadratu)


#WYRAŻENIA NA SŁOWNIKACH
temperaturaC = {'temp8': -10,
               'temp12': 0,
               'temp16': -10,
               'temp22': -26}

print("Temperatura w Celcjuszach: ", temperaturaC)


temperaturaF = {key: value * 1.8 + 32
                for key, value in temperaturaC.items()
                }

print("Temperatura w Fahrenheitach: ", temperaturaF)


#Generator list
import sys

parzyste3_bez_generatora = [element
                            for element in range(8000)
                            if (element % 2) == 0
                            ]
print(parzyste3_bez_generatora)
print(sys.getsizeof(parzyste3_bez_generatora))


parzyste3_z_generatorem = (element
                            for element in range(1000000)
                            if (element % 2) == 0
                           )

for item in parzyste3_z_generatorem:
    print(item)

print(parzyste3_z_generatorem)
print(sys.getsizeof(parzyste3_z_generatorem))