inc = 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("    ", end="")
    for k in range(inc, 0, -1):
        print(chr(k+64), end="  ")
    inc += 2
    print()