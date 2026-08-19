# Check Person can donate blood or not
# 1. Only Males, 2. Age => 18-55, 3. Weight => 50-90

gender = 'M'
age = 23
weight = 55

if gender == 'M':
    if age >= 18 and age <= 55:
        if weight >= 50 and weight <= 90:
            print("Can donate blood")
        else:
            print("Weight issue")
    else:
        print("Error : Age issue")
else:
    print("Error : Only Males Allowed")