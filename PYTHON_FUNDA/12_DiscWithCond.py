# Give 20% discount on minimum bill 5000

bill = int(input("Enter Bill : "))

if bill >= 5000:
    discount = 0.20 * bill
    bill = bill - discount

print(f"Pay : {bill}")