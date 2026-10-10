# Print number and its type
nums = [1, 2, 3, 4, 5]
result = [(x, "Even") if x % 2 == 0 else (x, "Odd") for x in nums]
print(result)