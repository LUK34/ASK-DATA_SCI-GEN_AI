# Character => Upper case / Lower Case / Digit / Symbol

ch = input("Enter Character : ")

if ch >= 'A' and ch <= 'Z':
    print("Upper case alphabet")
elif ch >= 'a' and ch <= 'z':
    print("Lower Case alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Symbol")