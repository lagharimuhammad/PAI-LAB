class Vehicle: 
    def __init__(self, seatingCap):
        self.seatingCap = seatingCap

    def fare(self):
        return self.seatingCap * 100
    
class Bus(Vehicle):
    def fare(self):
        baseFare = super().fare()
        return baseFare + 0.10*baseFare
    

v = Vehicle(4)
b = Bus(50)
print("Vehicle fare: ", v.fare())
print("Bus fare: ", b.fare())