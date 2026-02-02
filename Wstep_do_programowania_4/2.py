import math


def oblicz_pole_trapezu():

    try:
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        h = float(input("Podaj bok h: "))


        if a <= 0 and b <= 0 and h <= 0:
            print("Długosc boku nie może być ujemna!")
            return
        else:
            pole = ((a + b) * h) / 2.0
            print(f"Pole trapezu wynosi {pole:.2f}")
    except ValueError:
        print("Musisz podać liczbe")
oblicz_pole_trapezu()