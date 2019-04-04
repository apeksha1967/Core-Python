dec = 9
for i in range(5, 0, -1):
    for j in range(i, 5):
        print("  ", end="")
    print(str(dec)*dec)
    dec -= 2
