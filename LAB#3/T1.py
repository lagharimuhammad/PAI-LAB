def calculateArea(len, wid):
    return len * wid;

l = int(input("Enter length of rectangle: "))
w = int(input("Enter width of rectangle: "))

area = calculateArea(l,w)
print("Area: ", area)