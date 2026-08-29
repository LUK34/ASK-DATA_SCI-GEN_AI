n = int(input("Enter n val : "))

count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count+=1
        print(f"{i} is factor")

print(f"Count : {count}")