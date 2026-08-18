n = int(input("Enter num : "))

if n < 0:
    print("Error : Negative Num")
else:
    if n % 2 == 0:
        print("Even num")
    else:
        print("Not Even num")