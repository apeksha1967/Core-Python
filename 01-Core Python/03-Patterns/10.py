plus = 1
char = 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("  ", end="")
    print(str(char)*plus, end="")
    plus += 2
    char += 2
    print()