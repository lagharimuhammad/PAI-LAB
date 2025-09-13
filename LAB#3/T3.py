def employee( naam , salary = 10000):
    rate =  0.02 * salary
    salary = salary - rate

    print("Name: ", naam)
    print("Salary after Tax: ", salary)


naam = input("Enter your name: ")
salary = input("Enter your salary: ")

if salary == "":
    employee(naam)
else:
    employee(naam, float(salary))