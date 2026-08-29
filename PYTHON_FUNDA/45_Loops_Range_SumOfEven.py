count = 0
sum = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1
        sum = sum + i

print(f"Count is : {count}")
print(f"Sum is : {sum}")