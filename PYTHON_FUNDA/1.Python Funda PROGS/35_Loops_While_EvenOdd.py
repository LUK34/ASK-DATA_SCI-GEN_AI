while True:
    n = int(input("Enter num : "))
    if n % 2 == 0:
        print(f"{n} is EVEN")
    else:
        print(f"{n} is ODD")
    choice = input("Do you continue(y/n) : ")
    if choice == "n":
        break
