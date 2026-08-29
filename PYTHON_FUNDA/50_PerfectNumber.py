n = int(input("Enter n val : "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is Perfect")
else:
    print(f"{n} is not Perfect")

# When checking whether a number is perfect, the number itself must not be
# included in the sum.