plus = 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("   ", end="")
    print(" + "*plus, end="")
    plus += 2
    print()