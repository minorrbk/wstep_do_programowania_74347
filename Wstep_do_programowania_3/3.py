zdanie = input("Napisz słowo które chcesz sprawdzić czy jest palindromem: ")

zdaniebezspacji1 = "".join(zdanie.split())
zdaniebezspacji = zdaniebezspacji1.lower()
zdanieodtylu = zdaniebezspacji[::-1]

if zdanieodtylu == zdaniebezspacji:
    print("Jest to Palindrom")
else:
    print("Nie jest to Palindrom!")
