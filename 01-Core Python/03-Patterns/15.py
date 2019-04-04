for i in range(1, 6):
    for j in range(0, i+1):
        print("     ", end="")
    for k in range(i, 5):
        print(chr(k+64), end="   ")
    for l in range(5, i-1, -1):
        print(chr(l + 64), end="   ")
    print()