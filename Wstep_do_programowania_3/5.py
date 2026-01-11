Lista = {"chleb" : 4.99, "masło" : 6.01, "jajka" : 9.99, "skyr" : 4.69}

for przedmiot, cena in Lista.items():
    print(f"{przedmiot} : {cena:.2f}zł")

wydatek = sum(Lista.values())

print(f"Całkowita kwota to: {wydatek:.2f}")