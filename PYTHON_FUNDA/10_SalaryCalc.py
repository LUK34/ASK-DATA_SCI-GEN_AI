# Finding total salary for the given basic salary
# 13% HRA, 12% TA, 8% DA, 6% PF, 4% ESI

basic = int(input("Enter basic salary : "))

HRA = 0.13 * basic
TA = 0.12 * basic
DA = 0.08 * basic
PF = 0.06 * basic
ESI = 0.04 * basic

total = basic + HRA + TA + DA - PF - ESI

print(f"Total salary : {total}")

