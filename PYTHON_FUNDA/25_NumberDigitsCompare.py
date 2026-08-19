n = int(input("Enter num : "))

if 0 <= n <= 9:
    print("Single Digit Num")
elif 10 <= n <= 99:
    print("Two Digit Num")
elif 100 <= n <= 999:
    print("Three Digit Num")
else:
    print("Other Digit Num")