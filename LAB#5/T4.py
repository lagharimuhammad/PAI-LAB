def saveEmployee(fileName):
    try:
        with open(fileName, 'a') as file:
            name = input("Enter name: ")
            cnic = input("enter cnic: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))

        with open(fileName, 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")

    except PermissionError:
        print("Permsission denied")

    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print("unexpected error ", e)

def appendPhoneNumber(fileName):
    phoneNo = input("Enter phone Number: ")
    try:
        with open(fileName, 'a') as file:
            file.write(f"Phone Number: {phoneNo}\n")

    except PermissionError:
        print("Permsission denied")

    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print("unexpected error ", e)

def readEmployee(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print("Employee Details \n", content)

    except PermissionError:
        print("Permsission denied")

    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print("unexpected error ", e)

file = input("enter file name: ")
saveEmployee(file)
appendPhoneNumber(file)
readEmployee(file)