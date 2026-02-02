import time
import time


def sekundnik(sekundy):
    print(f"odliczanie {sekundy} sekund...")

    while sekundy > 0:

        print(f"Pozostało: {sekundy}")

        time.sleep(1)
        sekundy -= 1

    print("Pozostalo: 0 s   ")
    print("Koniec")

t = int(input("Podaj czas w sekundach: "))
sekundnik(t)