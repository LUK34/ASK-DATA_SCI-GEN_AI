ch = input("Enter Character : ")

if 'A' <= ch <= 'Z':
    print("Upper case alphabet")
elif 'a' <= ch <= 'z':
    print("Lower Case alphabet")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Symbol")