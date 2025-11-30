import math

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

if a > 0 and b > 0 and c > 0:

    obwod = a + b + c
    po = (a + b + c) / 2

    polekwadrat = po * (po - a) * (po - b) * (po - c)

    pole = math.sqrt(polekwadrat)

    print(f"Obwód wynosi: {obwod}")
    print(f"Pole wynosi: {pole}")

else:
    print("Dlugosc boku nie moze byc rowna lub mniejsza niz 0")