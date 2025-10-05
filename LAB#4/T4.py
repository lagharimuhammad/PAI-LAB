class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name

    def display(self):
        print(f"Student ID: {self.studentID}")
        print(f"Name: {self.name}")

class Marks(Student):
    def __init__ (self, studentID, name, marksAlgorithm, marksDS, marksCalculus):
        super().__init__(studentID, name)
        self.marksAlgorithm = float(marksAlgorithm)
        self.marksDS = float(marksDS)
        self.marksCalculus = float(marksCalculus)

    def displayM(self):
        print("Marks of Algorithm", self.marksAlgorithm)
        print("Marks of Data Science", self.marksDS)
        print("Marks of Calculus", self.marksCalculus)

class Result(Marks):
    def calculateTotal(self):
        return float(self.marksAlgorithm + self.marksCalculus + self.marksDS)
    
    def calculateAVG(self):
        return float(self.calculateTotal() / 3)
    
    def displayR(self):
        t = self.calculateTotal()
        a = self.calculateAVG()
        print("Total marks: ", t)
        print("Average: ", a)

r = Result("24K-0006", "Baqar", 87.6, 67.0, 96)
r.display()
r.displayM()
r.displayR()