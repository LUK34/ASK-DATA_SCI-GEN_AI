n = int(input("Enter n val : "))

factor_count = 0
proper_factor_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        factor_count += 1

        if i != n:
            proper_factor_sum += i

if n > 1 and factor_count == 2:
    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")

if n > 0 and proper_factor_sum == n:
    print(f"{n} is Perfect")
else:
    print(f"{n} is not Perfect")