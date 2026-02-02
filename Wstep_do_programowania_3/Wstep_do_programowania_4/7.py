import math


def obliczaniepola(a, b, c):
    try:

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Bok musi być liczbą dodatnią")

        if (a + b <= c) or (b + c <= a) or (c + a <= b):
            raise ValueError("Jeden bok nie może być dłuższy niż suma pozostałych")

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return round(pole, 2)

    except ValueError as e:

        return f"Błąd danych: {e}"



try:
    a = float(input("Podaj wartosc pierwszego boku: "))
    b = float(input("Podaj wartosc drugiego boku: "))
    c = float(input("Podaj wartosc trzeciego boku: "))

    wynik = obliczaniepola(a, b, c)

    print(f"Pole trójkąta to: {wynik}")

except ValueError:
    print("Błąd: Wprowadzono tekst zamiast liczby!")