

#Pętla for wymaga zmiennej po której będzie się poruszać
#można ją zdefiniować jako "i", ale w dobrym tonie jest
#aby użyć zmiennej "_", jeśli nigdzie nie będziemy wykorzystywać
#tej zmiennej w pętli

liczba = 100

def Fibbonaci(liczba):
    x, y = 0, 1

    for _ in range(liczba):
        x, y = y, x + y
        yield x

for item in Fibbonaci(liczba):
    print(item)