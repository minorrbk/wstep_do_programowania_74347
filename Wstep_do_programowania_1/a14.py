plik = input("Podaj pełną nazwe pliku: ")

if plik.endswith((".xlsx")):
    print("To jest plik arkusza Excel")
else:
    print("To nie jest plik arkusza Excel")

#Funkcja endswith pozwala sprawdzic czy koncowka nazwy pliku kończy się tak jak powinna.
