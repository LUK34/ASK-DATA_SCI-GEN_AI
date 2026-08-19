# Check Num => Single Digit / Two Digit / 3 Digit / Other digit

n = int(input("Enter num : "))

if n >= 0 and n <= 9:
    print("Single Digit Num")
elif n >= 10 and n <= 99:
    print("Two Digit Num")
elif n >= 100 and n <= 999:
    print("Three Digit Num")
else:
    print("Other Digit Num")