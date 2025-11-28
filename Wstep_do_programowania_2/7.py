print("a)")
imie = (input("Podaj imie: "))
print(f"Witaj, {imie}")

print("b)")
wiek = (input("Podaj swój wiek: "))
print(f"Twoj wiek to: {wiek}")

print("c)")
nazwisko = (input("Podaj swoje nazwisko: "))
print(imie[0], nazwisko[0])

print("d)")
for i in range(5):
    print(imie, nazwisko)

print("e)")
L1 = f"Mam na imie {imie},"
L2 = f" a na nazwisko {nazwisko}"
L3 = L1 + L2
print(L3)

print("f)")
Lancuch1 = f"Moje imie i nazwisko to: {imie}, {nazwisko}"
Lancuch2 = f"Mam {wiek} lat"

halflancuch1 = len(Lancuch1) // 2
halflancuch2 = len(Lancuch2) // 2
Lancuch3 = Lancuch1[:halflancuch1] + Lancuch2[:halflancuch2]
print(Lancuch3)