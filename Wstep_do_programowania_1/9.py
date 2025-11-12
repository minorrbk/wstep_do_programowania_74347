cenazwykla = 20
cenastudent = 20*0.75
cena4 = 0
cena4do18 = 10

wiek = int(input("Ile masz lat?: "))
if wiek <= 4:
    print(f"Cena za twój bilet wynosi {cena4}zł")
elif wiek > 4 and wiek < 18:
    print(f"Cena za twój bilet wynosi {cena4do18}zł")
elif wiek >= 18 and wiek < 150:
    student = input("Czy jesteś studentem? (Tak/Nie) ")
    if student == "tak" or student == "Tak":
        print(f"Cena twojego biletu wynosi: {cenastudent}")
    elif student == "nie" or student == "Nie":
        print(f"Cena twojego biletu wynosi: {cenazwykla}")
    else:
        print("Nie podałes odpowiedniej wartośći.")