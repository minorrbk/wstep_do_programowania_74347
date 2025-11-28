x = int(input("Podaj pierwsza liczbe calkowita: "))
y = int(input("Podaj drugą liczbe calkowita: "))
xy = x - y
step = 1


if x > y:
    while x >= y:
        print(y)
        y = y + step
elif y > x:
    while y >= x:
        print(x)
        x = x + step
elif x == y:
    print("Podales dwie takie same liczby.")