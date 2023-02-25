# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

#1 zbiór
print("Chorzy w ostatnim miesiącu, którzy mieszkają w dzielnicy Krzyki: ", chorzy_miesiac.intersection(krzyki))

#2 zbiór
#Osoby mieszkające w Centrum i na Krzykach
print(len(krzyki.union(centrum)))
print("Osoby mieszkające w Centrum i na Krzykach: ", krzyki.union(centrum), "a jest ich w sumie: ", len(krzyki.union(centrum)))

#3 zbiór
# nikt nie powinien mieszkać jendocześnie
# w centrum i na krzykach – jeśli tak, trzeba usunąć
print(len(krzyki.union(centrum)))
if len(krzyki.intersection(centrum)) != 0:
    skad_usuwamy = input("Mam duplikaty. Usunąć z Centrum (C) czy z Krzyków (K)")
    duplikaty = krzyki.intersection(centrum)
    if skad_usuwamy == "C":
        for x in duplikaty:
            centrum.remove(x)
            print("Usuwam: ", x)
    elif skad_usuwamy == "K":
        for x in duplikaty:
            krzyki.remove(x)
            print("Usuwam: ", x)

#4 zbiór
# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać

#5 zbiór
# pesele żeńskie mają ostatnią cyfrę parzystą, męskie – nieparzystą.
# zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ)

#6 zbiór
#wypiszmy kobiety z krzyków, które były chore w ostatnim roku

#7 zbiór
#wypiszmy mężczyzn z centrum, którzy NIE byli chorzy w ostatnim roku

#8 zbiór
#zabezpieczmy program
#wszystkie dane, które wprowadzamy muszą być poprawne
#sprawdźmy, czy wszystkie pesele w zbiorach są poprawne (4ro cyfrowe liczby)