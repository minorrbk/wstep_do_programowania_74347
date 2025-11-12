#funkcja input pozwala nam na otrzymanie danych od użytkownika, możemy od razu podać nasze pytanie bez konieczności używania funkcji print

a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))

pole = a * b
obwod =  2 * a + 2 * b

print(f"Pole prostokąta wynosi: {pole:.2f}")
print(f"Obwód prostokąta wynosi: {obwod:.2f}")