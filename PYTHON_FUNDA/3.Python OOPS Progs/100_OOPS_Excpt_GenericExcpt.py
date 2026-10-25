nums = [3, 8, 9, 0, 4, 6, 5, 2, 0]

try:
    x = int(input("Enter first loc : "))
    y = int(input("Enter second loc : "))

    a = nums[x]
    b = nums[y]

    c = a / b
    print(f"Quotient : {c}")
except Exception as msg:
    print(f"Exception : {msg}")