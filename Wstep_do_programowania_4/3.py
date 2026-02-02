def czy_liczba():
    try:
        liczba = float(input("podaj liczbe: "))
        if liczba < 0:
            print("Liczba jest ujemna")
        else:
            print("Liczba jest dodatnia")
    except ValueError:
        print("Musisz podac liczbe!")
czy_liczba()