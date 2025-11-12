'''
1- dodawanie
2- odejmowanie
3- mnozenie
4- dzielenie
5- potęgowanie
'''

a = float(input("Podaj 1 liczbe: "))

b = float(input("Podaj 2 liczbe: "))

print("1 - dodawanie\n 2 - odejmowanie\n 3 - mnożenie\n 4 - dzielenie\n 5 - potęgowanie")

d = int(input("Wybierz które działanie chcesz wykonać "))

if d == 1:
    wynik = a+b 
    print(f"Wynik dodawania: {wynik}")
elif d == 2:
    wynik = a-b
    print(f"Wynik odejmowania to: {wynik}")
elif d == 3:
    wynik = a*b 
    print(f"Wynik mnożenia to: {wynik}")
elif d == 4:
    wynik = a/b
   
    if b != 0:
        print(f"Wynik dzielenia to: {wynik}")
    else: 
        print("NIE MOZNA DZIELIC PRZEZ 0")
elif d == 5:
    wynik = a**b
    print(f"Wynik potęgowania to: {wynik}")
else:
    print("NIE UZYLES POPRAWNEJ LICZBY")