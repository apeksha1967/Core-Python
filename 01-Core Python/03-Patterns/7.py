for i in range(0, 6):
    for j in range(5, i-1, -1):
        print(" ", end=" ")
        if i == j:
            print(str(i)*j, end="")
    print()