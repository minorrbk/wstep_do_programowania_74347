w = int(input("Podaj ilość gwiazdek: "))
"""
for i in range(1, w+1):
    print("*  "*w)


for i in range(1, w+1):
    for j in range(1, w+1):
        print("*  ", end="")
    print("")
   """

    # B
"""
for i in range(1, w+1):
    for j in range(1, ( (w+1) - (w - i) ) ):
        print("*  ", end="")
    print("")
"""

    # C
for i in range(1, w + 1):
    print(" " * (w - i) + "* " * i)