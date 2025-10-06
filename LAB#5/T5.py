import json

def savePeople(filename):
    try:
        people = {}
        n = int(input("Enter number of people: "))

        for i in range(n):
            name = input(f"Enter name: ")
            age = int(input(f"Enter age: "))
            people[name] = age

        with open(filename, 'w') as file:
            json.dump(people, file)

        with open(filename, 'r') as file:
            data = json.load(file)

        mostAged = max(data.values())
        print("\n")
        for name, age in data.items():
            if age == mostAged:
                print(name, "-", age)
        print("\n");
        
        print("same age:")
        checked = []
        for n1, a1 in data.items():
            for n2, a2 in data.items():
                if n1 != n2 and a1 == a2 and a1 not in checked:
                    print(n1, "and", n2, "have same age", a1)
                    checked.append(a1)

    except FileNotFoundError:
        print("Error, file not found.")
    except PermissionError:
        print("Error, permission denied.")
    except Exception as e:
        print("Unexpected error: ", e)

filename = 'people.json'
savePeople(filename)
