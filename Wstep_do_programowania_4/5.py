def srednia(liczby):
    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

uzytkownik = input("Podaj liczby oddzielone spacja: ")

try:
    liczbyuzytkownik = [float(x) for x in uzytkownik.split()]

    wynik = srednia(liczbyuzytkownik)
    print(f"Srednia wynosi: {wynik:.2f}")
except ValueError:
    print("Musisz podac liczby w odpowiednim formacie")