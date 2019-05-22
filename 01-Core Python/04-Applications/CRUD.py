studentList = []

students = {}

def create():
    print("Create Student Record...")
    studentId = int(input("Enter ID : "))
    studentName = input("Enter name : ")
    studentCourse = input("Enter course : ")
    studentNo = int(input("Enter number : "))

    students["Id"] = studentId
    students["Name"] = studentName
    students["Course"] = studentCourse
    students["No"] = studentNo

    # studentList.append([studentId, studentName, studentCourse, studentNo])
    studentList.append(students.copy())
    for s in studentList:
        print(s)

def read():
    print("Read Student Record...")
    for s in studentList:
        print(s)

def update():
    print("Update Student Record...")
    studentId = int(input("Enter Student ID you want to update data about : "))
    for i in range(len(studentList)):
        if studentList[i]['Id'] == studentId:
            print(studentList[i])
            print("Data you want to update: ")
            print("""
            1. Name
            2. Course
            3. Number
            """)
            choice = int(input("Enter your choice : "))
            if choice == 1:
                new_name = input("Enter updated Name:")
                studentList[i]['Name'] = new_name
            elif choice == 2:
                new_course = input("Enter updated Course:")
                studentList[i]['Course'] = new_course
            elif choice == 3:
                new_number = input("Enter updated Number:")
                studentList[i]['No'] = new_number
        else:
            pass

def delete():
    print("Delete Student Record...")
    studentId = int(input("Enter Student ID you want to delete : "))
    for i in range(len(studentList)):
        if studentList[i]['Id'] == studentId:
            print("Student Exist")
            del studentList[i]
            print("Deleted Successfully...")
            print("Updated List...")
            read()
        else:
            pass

def search():
    print("Search Student Record...")
    studentId = int(input("Enter Student ID you want to search : "))
    for i in range(len(studentList)):
        if studentList[i]['Id'] == studentId:
            print(studentList[i])
        else:
            pass

def sortStudents():
    print("Sort Student Record...")
    print("""
    1. Name
    2. Id
    """)
    order = int(input("Enter the order you want to sort the data:"))
    if order == 1:
        sortedList = sorted(studentList, key=lambda x : x["Name"])
        for s in sortedList:
            print(s)
    elif order == 2:
        sortedList = sorted(studentList, key=lambda x : x["Id"])
        for s in sortedList:
            print(s)
    else:
        print("Incorrect option..")

def save():
    with open("students.txt", "a") as file:
        # file.write(str(studentList))
        for data in studentList:
            formattedData = str(data).strip("{}")
            file.write(formattedData + "\n")

#def load():
#    print("Load Student Record...")
#    filename = input("Enter the name of file you want to load data from:")
#    raw_data = open(filename,'rt')
#    data = numpy.loadtxt(raw_data, delimiter=",")
#    print("Shape of data: ",data.shape)
#    studentList.append(data)
#    print("Shape of Student Record: ",len(studentList))

while True:
    print("""
    1. Create Record
    2. Read Record
    3. Update Record
    4. Delete Record
    5. Search Record
    6. Sort Record
    7. Save Record
    8. Quit
    """)

    todo = {
        "1": create,
        "2": read,
        "3": update,
        "4": delete,
        "5": search,
        "6": sortStudents,
        "7": save,
        "8": quit
    }

    userChoice = input("Enter your choice : ")

    todo.get(userChoice)()