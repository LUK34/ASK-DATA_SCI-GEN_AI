# Identify a shape using the number of sides

sides = int(input("Enter num of sides : "))

if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Rectangle")
elif sides == 5:
    print("Pentagon")
else:
    print("Other shape")