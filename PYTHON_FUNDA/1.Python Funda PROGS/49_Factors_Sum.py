n = int(input("Enter n val : "))

total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(f"Sum of factors : {total}")


# For `6`:
# Factors = 1, 2, 3, 6
# 1 + 2 + 3 + 6 = 12
