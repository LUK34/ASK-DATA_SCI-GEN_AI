start = int(input("Where to Start : "))
stop = int(input("Where to Stop : "))
step = int(input("Step:"))

print("Begin to End : ")

for i in range(start, stop + 1, step):
    print(f"i val : {i}")

print("End to Begin : ")

for j in range(stop, start - 1, -step):
    print(f"j val : {j}")