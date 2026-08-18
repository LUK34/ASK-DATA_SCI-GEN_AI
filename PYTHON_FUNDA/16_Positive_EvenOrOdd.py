# Nested if: writing an if block inside another if block
# Check whether the number is even or not (check only positive numbers)

n = int(input("Enter num : "))

if n > 0:
    if n % 2 == 0:
        print("Even num")
    else:
        print("Not Even num")
else:
    print("Error : Negative Num")