x = float(input("Podaj wartość x: "))

# A)
if x > 0:
    xa =  2 * x
elif x == 0:
    xa = 0
elif x < 0:
    xa = -3 * x 

# B)
if x >= 1:
    xb = x ** 2
elif x < 1:
    xb = x

# C)
if x > 2:
    xc = 2 + x
elif x == 2:
    xc = 8
elif x < 2: 
    xc = x - 4

print(f"Wyniki to: A = {xa}, B = {xb}, C = {xc}")

