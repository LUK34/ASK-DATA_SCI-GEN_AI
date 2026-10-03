lower = int(input("Where to start : "))
upper = int(input("Where to end : "))

for n in range(lower, upper + 1):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")