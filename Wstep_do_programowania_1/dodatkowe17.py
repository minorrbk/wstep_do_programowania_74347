znak = str(input("Napisz jedną litere: "))

dlugosc = len(znak)
if not znak.isalpha(): #is.alpha sprawdza czy uzytkownik podał cos innego niz litere.
    print("Miała byc litera.")
elif znak.isalpha():
    if len(znak) != 1:
        print("Miała być tylko jedna litera. ")
    else:

        kod = ord(znak)

        duze = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
                        89, 90,
                        260, 262, 280, 321, 323, 211, 346, 377, 379]
        male = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                        117, 118, 119, 120, 121, 122,
                        261, 263, 281, 322, 324, 243, 347, 378, 380]
        if kod in duze:
            print("Jest to duża litera")
        else:
            print("Jest to mała litera")

