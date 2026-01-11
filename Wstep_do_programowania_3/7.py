import math
import random
from operator import truediv

a = random.randint(3,7)
b = random.randint(3,7)

ilosc = random.randint(3, 10)

zbiorx = set()

while len(zbiorx) < a:
    liczby = random.randint(0,10)
    zbiorx.add(liczby)

zbiory = set()

while len(zbiory) < b:
    liczby = random.randint(0,10)
    zbiory.add(liczby)
print(f"zbiór x to: {zbiorx}")
print(f"zbiór y to: {zbiory}")


print("-"*35)

print("sprawdzenie czy liczba 5 występuje w zbiorze x")
if 5 in zbiorx:
    print("5 znajduje się w zbiorze x")
else:
    print("5 nie występuje w zbiorze x")

print("-"*35)

print("Sprawdzenie czy zbiór x jest podzbiorem zbioru y")

if zbiorx.issubset(zbiory):
    print("Tak, zbior x jest podzbiorem zbioru y")
else:
    print("Nie, zbior x nie jest podzbiorem zbioru y")

print("-"*35)

print("Sprawdzenie czy zbiór y jest podzbiorem zbioru x")

if zbiory.issubset(zbiorx):
    print("Tak, zbior y jest podzbiorem zbioru x")
else:
    print("Nie, zbior y nie jest podzbiorem zbioru x")

print("-"*35)

sumaxy = zbiorx.union(zbiory)
print(f"Suma zbiorow x i y to: {sumaxy}")
print("-"*35)

roznicaxy = zbiorx.difference(zbiory)
print(f"roznica zbiorów x oraz y to: {roznicaxy}")
print("-"*35)

roznicayx = zbiory.difference(zbiorx)
print(f"roznica zbiorów y oraz x to: {roznicayx}")
print("-"*35)

iloczynxy = zbiorx.intersection(zbiory)
print(f"Iloczyn zbiorów x oraz y to: {iloczynxy}")
print("-"*35)

maxx = max(zbiorx)
maxy = max(zbiory)

print(f"Maksymalna wartosc w zbiorze x to {maxx}")
print(f"Maksymalna wartosc w zbiorze y to {maxy}")
print("-"*35)

zbiory.add(zbiorx.pop())
print(f"zbior x: {zbiorx}")
print(f"zbior y: {zbiory}")

print("-"*35)

zbiory.update(zbiorx)

print(f"Zbiór y: {zbiory}")
print(f"Zbiór x: {zbiorx}")

print("-"*35)

zbiorx.clear()
zbiory.clear()

print(f"zbior x: {zbiorx}")
print(f"zbior y: {zbiory}")