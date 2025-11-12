cena = 6.5
droga = float(input("Podaj długość trasy: "))
spalanie = float(input("Podaj średnie spalanie: "))

zpaliwa = (droga * spalanie) / 100
cpaliwa = (droga * spalanie * cena) / 100

print(f"Zużycie paliwa na danej trasie wynosi: {zpaliwa:.2f}")
print(f"Cena paliwa na danej trasie wynosi: {cpaliwa:.2f}")