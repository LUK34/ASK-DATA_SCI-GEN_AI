# 1. Find doubles
nums = [1, 2, 3, 4, 5]
result = [x * 2 for x in nums]
print(result)

# 2. Find even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x for x in nums if x % 2 == 0]
print(result)

# 3. Add 5 to each number
nums = [1, 2, 3, 4, 5]
result = [x + 5 for x in nums]
print(result)

# 4. Find squares of even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x ** 2 for x in nums if x % 2 == 0]
print(result)

# 5. Label each number as even or odd
nums = [1, 2, 3, 4, 5]
result = [(x, "Even") if x % 2 == 0 else (x, "Odd") for x in nums]
print(result)

# 6. Work with strings
words = ["python", "java", "react", "sql", "flask"]

res = [x for x in words]
print(res)

res = [x.upper() for x in words]
print(res)

res = [len(x) for x in words]
print(res)

res = [(x, len(x)) for x in words]
print(res)

res = [x for x in words if len(x) > 5]
print(res)

res = [x[0] for x in words]
print(res)

res = [x[-1] for x in words]
print(res)