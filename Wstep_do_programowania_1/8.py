wiek = int(input("Napisz ile masz lat: "))

if wiek > 0 and wiek < 150:
    if wiek > 0 and wiek < 18:
        print("Jesteś niepełnoletni")
    if wiek >= 18 and wiek < 150:
        print("Jesteś pełnoletni")
else:
    print("Podałes nieprawdziwą wartość")