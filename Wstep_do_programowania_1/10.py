x = float(input("Podaj wartość x: "))
z = float(input("Podaj wartość z: "))
y = float(input("Podaj wartość y: "))

# x,z,y x,y,z z,x,y z,y,x y,x,z y,z,x

if x <= z and z <= y:
    print(f"Kolejność liczb od najmniejszej do największej to:{x}, {z}, {y} ")
elif x <= y and y <= z:
    print(f"Kolejność liczb od najmniejszej do największej to:{x}, {y}, {z} ")
elif z <= x and x <= y:
    print(f"Kolejność liczb od najmniejszej do największej to:{z}, {x}, {y} ")
elif z <= y and y <= x:
    print(f"Kolejność liczb od najmniejszej do największej to:{z}, {y}, {x} ")
elif y <= x and x <= z:
    print(f"Kolejność liczb od najmniejszej do największej to:{y}, {x}, {z} ")
elif y <= z and z <= x:
    print(f"Kolejność liczb od najmniejszej do największej to:{y}, {z}, {x} ")