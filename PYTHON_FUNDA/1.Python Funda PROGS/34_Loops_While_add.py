while True:
    a = int(input("Enter First num : "))
    b = int(input("Enter Second num : "))
    c = a + b
    print(f"Sum = {c}")
    choice = input("Do you stop(y/n) : ")
    if choice == "y":
        break