a = float(input("Podaj wartosc a:"))
b = float(input("Podaj wartosc b:"))

if a != 0:
    x = - b / a
    print(f"Rozwiązanie x wynosi: {x}")
else:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań")
    else:
        print("Równanie sprzeczne")
