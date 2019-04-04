for i in range(3, -4, -1):
    for j in range(abs(i), 0, -1):
        print("  ", end="")
    for k in range(3, abs(i)-1, -1):
        print(chr(k+65), end="")
    print()