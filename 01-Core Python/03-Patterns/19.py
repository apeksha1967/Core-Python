for i in range(3, -4, -1):
    for j in range(abs(i), 0, -1):
        print("   ", end=" ")
    for k in range(abs(i), 4):
        print("*  ", end="")
    print()