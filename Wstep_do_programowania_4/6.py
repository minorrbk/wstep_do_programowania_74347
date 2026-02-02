def wypisz_dane(imie, wiek=20):

    print(f"Imię: {imie}, Wiek: {wiek}")

print("Dokumentacja funkcji (a)")
print(wypisz_dane.__doc__)

print("\nWywołanie z podaniem wieku")
wypisz_dane("Kasia", 35)

print("\nWywołanie bez podania wieku (b)")
wypisz_dane("Tomek")