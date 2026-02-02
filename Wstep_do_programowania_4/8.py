def potega_rek(a, n):

    if n == 0:
        return 1

    elif n < 0:
        return 1 / potega_rek(a, -n)

    else:
        return a * potega_rek(a, n - 1)



podstawa = int(input("Podaj wartosc podstawy "))
wykladnik = float(input("Podaj wartosc wykladnika "))

wynik = potega_rek(podstawa, wykladnik)
print(f"{podstawa} do potęgi {wykladnik} wynosi: {wynik}")

print(f"{potega_rek(podstawa, wykladnik)}")