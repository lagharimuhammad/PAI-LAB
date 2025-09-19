students = {"Ahmed": 93.0, "Ali":78.2, "Jahanzaib": 88.56}
while True:    
    print("1. Add Students \t2. Change Marks \t3. Remove Student \t4. Show Topper \t5. Display all Students \n6. Exit")

    choice = int(input("Enter your action: "))
                       

    if(choice == 1):
        x = int(input("How many students you wanna add: "))

        for n in range(x):
            name = input("Enter student name: ")
            mark = float(input("Enter their number: "))

            students[name] = mark

    elif(choice == 2):
        x = input("Which student marks you wanna update: ")
        if x in students:
            new = float(input("Enter new marks: "))
            students[x] = new
        else:
            print("Not found")

    elif(choice == 3):
        delete = input("Which student you wanna delete: ")
        if delete in students:
            del students[delete]
        else:
            print("Not found")

    elif(choice == 4):
        topper = None
        numTop = 00.00

        for key, value in students.items():
            if(numTop < value):
                numTop = value
                topper = key

        print(f"The topper is {topper} with splendid numbers of {numTop}")

    elif(choice == 5):
        print(students)

    elif(choice == 6):
        break

    else:

        print("Wrong input.")

