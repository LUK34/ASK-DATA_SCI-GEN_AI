first = int(input("Enter first number in range : "))
second = int(input("Enter second number in range : "))

for n in range(first, second):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print(n)