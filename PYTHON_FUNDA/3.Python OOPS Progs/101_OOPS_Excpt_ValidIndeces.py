nums = [3, 8, 9, 0, 4, 6, 5, 2, 0]

try:
    x = int(input("First index: "))
    y = int(input("Second index: "))

    if not (0 <= x < len(nums) and 0 <= y < len(nums)):
        raise IndexError("Indices must be between 0 and 8")

    print(f"Quotient: {nums[x] / nums[y]}")
except ValueError:
    print("Enter integer indices only")
except IndexError as error:
    print(f"Invalid index: {error}")
except ZeroDivisionError:
    print("Cannot divide by zero")