try:
    a = int(input("Enter first num : "))
    b = int(input("Enter second num : "))
    c = a + b
    print(f"Sum = {c}")
except ValueError:
    print("Exception : Input is Invalid")