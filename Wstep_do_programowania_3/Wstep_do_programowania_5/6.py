import math
import keyword


def pokaz_zawartosc(nazwa, obiekt):
    print(f"{nazwa.upper()}")

    wszystkie = dir(obiekt)

    publiczne = [nazwa for nazwa in wszystkie if not nazwa.startswith("__")]

    print(", ".join(publiczne))
    print("")

pokaz_zawartosc("math", math)

pokaz_zawartosc("tuple", tuple)

pokaz_zawartosc("keyword", keyword)