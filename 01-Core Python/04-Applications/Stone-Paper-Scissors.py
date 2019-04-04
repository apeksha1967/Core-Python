import random

options = ['stone', 'paper', 'scissor']

userCounter = 0
cpuCounter = 0

while True:

    cpuChoice = random.choice(options)

    userChoice = input("Enter your choice : ")
    print("CPU : ",cpuChoice)

    if userChoice == cpuChoice:
        print("Match Tie")

    elif userChoice == "paper" and cpuChoice == "stone":
        print("User win")
        userCounter += 1
        print("User :",userCounter)

    elif userChoice == "stone" and cpuChoice == "scissor":
        print("User win")
        userCounter += 1
        print("User :",userCounter)

    elif userChoice == "scissor" and cpuChoice == "paper":
        print("User win")
        userCounter += 1
        print("User :",userCounter)

    elif userChoice == "paper" and cpuChoice == "scissor":
        print("CPU win")
        cpuCounter += 1
        print("CPU :",cpuCounter)

    elif userChoice == "scissor" and cpuChoice == "stone":
        print("CPU win")
        cpuCounter += 1
        print("CPU :",cpuCounter)

    elif userChoice == "stone" and cpuChoice == "paper":
        print("CPU win")
        cpuCounter += 1
        print("CPU :",cpuCounter)

    else:
        print("Wrong Choice...")

    if userChoice == "q":
        print("Final Scores...")
        print("User : {}   CPU : {}".format(userCounter, cpuCounter))
        break
