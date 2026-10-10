while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter choice : "))

    if choice == 1:
        print("Enter 2 nums to add : ")
        a = int(input())
        b = int(input())
        print(f"Sum = {a + b}")

    elif choice == 2:
        print("Enter 2 nums to subtract : ")
        a = int(input())
        b = int(input())
        print(f"Difference = {a - b}")

    elif choice == 3:
        print("Enter 2 nums to multiply : ")
        a = int(input())
        b = int(input())
        print(f"Product = {a * b}")

    elif choice == 4:
        print("Enter 2 nums to divide : ")
        a = int(input())
        b = int(input())
        print(f"Product = {a / b}")

    elif choice == 5:
        print("Enter 2 nums to modulus : ")
        a = int(input())
        b = int(input())
        print(f"Product = {a % b}")

    elif choice == 6:
        print("End")
        break

    else:
        print("Error : Invalid choice")