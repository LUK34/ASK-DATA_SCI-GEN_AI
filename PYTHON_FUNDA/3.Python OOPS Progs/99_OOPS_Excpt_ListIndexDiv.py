# Index:  0  1  2  3  4  5  6  7  8
nums = [3, 8, 9, 0, 4, 6, 5, 2, 0]

try:
    x = int(input("Enter first loc : "))
    y = int(input("Enter second loc : "))

    a = nums[x]
    b = nums[y]

    c = a / b
    print(f"Quotient : {c}")

except ValueError:
    print("Exception : Invalid locs")
except IndexError:
    print("Exception : Out of Bounds")
except ZeroDivisionError:
    print("Exception : cannot divide by 0")