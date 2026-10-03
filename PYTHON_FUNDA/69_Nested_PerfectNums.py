for n in range(1, 10000):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if n == sum:
        print(f"{n} is Perfect")