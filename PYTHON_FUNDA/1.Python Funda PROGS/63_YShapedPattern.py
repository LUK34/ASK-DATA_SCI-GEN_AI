for i in range(1, 10):

    for j in range(1, 10):

        if ((i == j and i <= 5) or
            (i + j == 10 and i <= 5) or
            (j == 5 and i >= 5)):

            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()