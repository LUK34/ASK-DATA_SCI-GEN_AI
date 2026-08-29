n = int(input("Enter n val : "))

count = 0
total = 0

print(f"Factors of {n}:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count += 1
        total += i

print(f"Number of factors : {count}")
print(f"Sum of factors    : {total}")