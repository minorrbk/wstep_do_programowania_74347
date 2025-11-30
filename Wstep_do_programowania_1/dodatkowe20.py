gol = int(input("Podaj ilość bramek: "))
bonus = int(input("Podaj bonus: "))

punkty = gol * 10

if gol > 5:
    punkty +=5
if gol > 10:
    punkty +=10

punkty += bonus
print(f"Łączna ilosc punktow to {punkty}")