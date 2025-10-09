class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)

    def calculateBonus(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculateBonus(self):
        return self.salary * 0.20

    def hire(self, personName="someone"):
        print(f"{self.name} is hiring {personName}.")


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculateBonus(self):
        return self.salary * 0.10

    def writeCode(self, feature="a feature"):
        print(f"{self.name} is writing code for {feature}.")


class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculateBonus(self):
        return self.salary * 0.30


    m = Manager("Omer", 100000)
    d = Developer("Kashif", 80000)
    s = SeniorManager("Baqar", 150000)

    print(f"{m.name} bonus: ${m.calculateBonus():.2f}")
    m.hire("Umair")

    print(f"{d.name} bonus: ${d.calculateBonus():.2f}")
    d.writeCode("Database System")

    print(f"{s.name} bonus: ${s.calculateBonus():.2f}")

    s.hire("Burhan")
