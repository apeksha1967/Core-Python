plus = 1
char = 65
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("  ", end="")
    print(chr(char)*plus, end="")
    plus += 2
    char += 1
    print() 