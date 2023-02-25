print("hejka")

student = {'Name': "John",
           'Age': 23,
           'Height': 180.5,
           0: 'zero'}

print(type(student))
print(student)

print(student["Name"])
print(student[0])

for key in student.keys():
    print("klucz to: ", key)

#Printowanie w petli po calych itemsach
for key, values in student.items():
    print("Dla klucza: ", key, " wartość to: ", values)

#inny przykład
a, b = 5, 10
print(a, b)

#ZADANIE 1
#użytkownik będzie mógł dodawać nowe
#pozycje do slownika

definicje = {}

while True:
    print("1. Dodaj nową definicję")
    print("2. Znajdź definicję")
    print("3. Usuń definicję")
    print("4. Zakończ")
    print("")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1":
        klucz = input("Podaj słowo, które chcesz zdefiniować: ")
        definicja = input("Podaj definicję tego słowa: ")
        definicje[klucz] = definicja
    elif wybor == "2":
        klucz = input("Czego sukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Przykro mi, nie wiem co to.")
    elif wybor == "3":
        klucz = input("Co chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunięto: ", klucz)
        else:
            print("Przykro mi, nie ma takiego wpisu.")
    elif wybor == "4":
        break

