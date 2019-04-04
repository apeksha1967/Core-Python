options = [["[123, 'john', 123, 'john']", "[123, 'john'] * 2", "Error", "None of the above."],
           ["islower()", "isnumeric()", "isspace()", "istitle()"],
           ["shuffle(lst)", "capitalize()", "isalnum()", "isdigit()"],
           ["cmp(list)", "len(list)", "max(list)", "min(list)"]]

answers = ["[123, 'john', 123, 'john']", "isnumeric()", "shuffle(lst)", "min(list)"]

with open('questions.txt') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        print(lines[i])
        # print(options[i])
        op = options[i]
        for j in op:
            print(j)

        userInput = input("Enter your ans : ")

        if userInput == answers[i]:
            print("Correct Ans...")
        else:
            print("Wrong Ans...")
            break
