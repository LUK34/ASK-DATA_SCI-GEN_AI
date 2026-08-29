n = int(input("Enter n val : "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if n > 1 and count == 2:
    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")