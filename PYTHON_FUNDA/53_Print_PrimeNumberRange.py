first = int(input("Enter first number in range : "))
second = int(input("Enter second number in range : "))

for n in range(first , second):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n)