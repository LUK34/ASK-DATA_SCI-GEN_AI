n = int(input("Enter n val : "))

print("---------------------------------")
print("FORWARD Direction:")
print("1-n nums : ")
for i in range(1, n + 1, 1):
    print(f"i val : {i}")

print("---------------------------------")
print("BACKWARD Direction:")
print("n-1 nums : ")
for j in range(n, 0, -1):
    print(f"j val : {j}")

print("---------------------------------")