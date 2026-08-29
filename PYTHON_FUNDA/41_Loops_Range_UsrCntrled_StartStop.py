start = int(input("Where to Start : "))
stop = int(input("Where to Stop : "))

print("Start to Stop : ")

for i in range(start, stop + 1, 1):
    print(f"i val : {i}")

print("End to Begin : ")

for j in range(stop, start - 1, -1):
    print(f"j val : {j}")