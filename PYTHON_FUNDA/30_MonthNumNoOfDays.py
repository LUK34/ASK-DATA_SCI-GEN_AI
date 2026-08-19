# Read Month Num => Display Num of Days

m = int(input("Enter month num : "))

if m >= 1 and m <= 12:
    if m == 2:
        print("28/29 days")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("30 days")
    else:
        print("31 days")
else:
    print("Invalid Month")