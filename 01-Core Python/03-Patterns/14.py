for i in range(1, 6):
    for j in range(i, 6):
        print("     ", end="")
    for k in range(i-1, -i, -1):
        print(str(i-abs(k)), end="   ")
    print()