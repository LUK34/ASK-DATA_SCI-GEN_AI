# Check Student Pass (then display grade) or Failed

m1 = 67
m2 = 56
m3 = 72

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    avg = (m1 + m2 + m3) / 3

    if avg >= 75:
        print("Grade-A")
    elif avg >= 60:
        print("Grade-B")
    else:
        print("Grade-C")
else:
    print("Failed")