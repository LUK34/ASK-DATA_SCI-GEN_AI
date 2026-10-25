try:
    a = int(input("Enter first num : "))
    b = int(input("Enter second num : "))
    c = a / b
    print(f"Quotient = {c}")
except ValueError:
    print("Exception : Input is Invalid")
except ZeroDivisionError:
    print("Exception : Denominator cannot be zero")