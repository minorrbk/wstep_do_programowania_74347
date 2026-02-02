def bmi():
    try:
        waga = float(input("podaj swoja wage w kilogramach: "))
        wzrost = float(input("podaj swoj wzrost w centymetrach: "))

        if waga > 30 and waga < 300 and wzrost > 70 and wzrost < 250:
            bmi = waga / ((wzrost * 0.01) ** 2)
            if bmi < 18.5:
                print("Niedowaga!")
            if bmi > 18.5 and bmi < 24.9:
                print("Waga prawidłowa!")
            if bmi > 25.0:
                print("Nadwaga!")
        else:
            print("Podaj prawdziwe dane!")



    except ValueError:
            print("Musisz podac liczbe!")
bmi()