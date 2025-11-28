import math


a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

delta = b ** 2 - 4 * (a * c)

if delta < 0:
    print("Nie ma rozwiązań dla ujemnej delty")
if delta == 0:
    x0 = -b / (2 * a)
    print(f"Jest jedno miejsce zerowe: {x0}")
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Są dwa miejsca zerowe: {x1} oraz {x2}")
