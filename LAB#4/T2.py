from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self):
        return self.length* self.width
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def area(self):
        return self.base* self.height * 0.5
    

class Square(Shape):
    def __init__(self, side):
        self.side = float(side)

    def area(self):
        return self.side ** 2
    
r = Rectangle(5,4)
t = Triangle(3,8)
s = Square(7)
print("Area of rectangle: ", r.area())
print("Area of tritangle: ", t.area())
print("Area of square: ", s.area())