def big(a, b, c):
    if a > b and a > c:
        print("a is big")
    elif b > c:
        print("b is big")
    else:
        print("c is big")
    return

print("Enter 3 nums : ")

x = int(input())
y = int(input())
z = int(input())

big(x, y, z)