import math


def oblicz_pole_kola():

    try:
        r = float(input("Promien kola: "))
        if r <= 0:
            print("Promień nie może być ujemny!")
            return
        else:
            pole = math.pi * r ** 2
            print(f"Pole koła o promieniu {r} wynosi {pole:.2f}")
    except ValueError:
        print("Musisz podać liczbe")
oblicz_pole_kola()