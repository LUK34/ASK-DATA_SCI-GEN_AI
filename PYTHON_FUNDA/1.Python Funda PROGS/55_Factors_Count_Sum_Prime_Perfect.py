n = int(input("Enter a number : "))

factor_count = 0
factor_sum = 0
proper_factor_sum = 0

print(f"\nFactors of {n}:")

for i in range(1, n + 1):

    if n % i == 0:

        print(i)

        factor_count += 1
        factor_sum += i

        if i != n:
            proper_factor_sum += i


print(f"\nFactor count : {factor_count}")
print(f"Factor sum   : {factor_sum}")


# Prime Number Check

if n > 1 and factor_count == 2:
    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")


# Perfect Number Check

if n > 0 and proper_factor_sum == n:
    print(f"{n} is Perfect")
else:
    print(f"{n} is not Perfect")


