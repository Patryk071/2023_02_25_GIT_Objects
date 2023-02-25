import random

#Losowanie 6 liczb (niepowtarzających się)
#ze zbioru 49 liczb - od 1 do 49
#Aby wyniki się nie powtarzały to zastosuje
#funckję random.sample
def wylosuj_liczby(ile, wielkosc_zbioru):
    print(random.sample(range(wielkosc_zbioru + 1), ile))

wylosuj_liczby(6, 49)

#Mamy talię kart, którą chcemy przetasować
#A następnie rozdać je dla 2 graczy (po  kart)
talia = ["9", "9", "9", "9",
         "10", "10", "10", "10",
         "Jopek", "Jopek", "Jopek", "Jopek",
         "Dama", "Dama", "Dama", "Dama",
         "Król", "Król", "Król", "Król",
         "As", "As", "As", "As"]

random.shuffle(talia)
print(talia)
print(len(talia))
print("")

karty_1_gracza = []
karty_2_gracza = []
i = 0

while i < 5:
    karty_1_gracza.append(talia.pop())
    karty_2_gracza.append(talia.pop())
    i += 1

#print("Karta dla pierwszego gracza: ", talia.pop())
#print("Karta dla drugiego gracza: ", talia.pop())

print("Karty pierwszego gracza: ", karty_1_gracza)
print("Karty drugiego gracza: ", karty_2_gracza)

print("")
print(talia)
print(len(talia))