
#a
zdanie = input("Napisz jakieś zdanie: ").lower()
litery = [litera1.lower() for litera1 in zdanie if litera1.isalpha()]
wlitery = [litera.lower() for litera in zdanie if litera.isalpha()]
wlitery.sort()
print(f"Litery w kolejności alfabetycznej to {wlitery}")

#b

nieparzystelitery = litery[::2]
print(f"Litery z parzystym indeksem to{nieparzystelitery}")

#c

slowa = zdanie.split()


duzelitery = [(s[0].upper() + s[1:-1].lower() + s[-1].upper()) for s in slowa]
print(duzelitery)

#d

nslowo = max(slowa, key=len)
print(f"Najdłuższe słowo to: {nslowo}")
print(f"jego długosc to: {len(nslowo)}")

#e

widziane = set()
koniec = ""
for znak in zdanie:
    l_test = znak.lower()
    if l_test.isalpha() and l_test in widziane:
        koniec += "@"
    else:
        koniec += znak
        if l_test.isalpha():
            widziane.add(l_test)

print(f"Zdanie po zmianie liter: {koniec}")