from abc import ABC
from datetime import date

class RentalVehicle(ABC):
    def __init__(self, make, model, rental_price_per_day):
        self.make = make
        self.model = model
        self.__rental_price_per_day = float(rental_price_per_day)  
        self.__available = True  

    @property
    def rental_price_per_day(self):
        return self.__rental_price_per_day

    @rental_price_per_day.setter
    def rental_price_per_day(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("rental_price_per_day must be positive")
        self.__rental_price_per_day = value

    def check_availability(self):
        return self.__available

    def rent(self):
        if not self.__available:
            raise RuntimeError("Vehicle is not available.")
        self.__available = False

    def return_vehicle(self):
        self.__available = True

    def calculate_rental_cost(self, start_date, end_date):
        if not isinstance(start_date, date) or not isinstance(end_date, date):
            raise TypeError("start_date and end_date must be datetime.date instances")
        days = (end_date - start_date).days + 1
        if days <= 0:
            raise ValueError("end_date must be on or after start_date")
        return days * self.__rental_price_per_day

    def display_details(self):
        print(f"{self.__class__.__name__}: {self.make} {self.model} | ${self.__rental_price_per_day:.2f}/day | Available: {self.__available}")


class Car(RentalVehicle):
    pass

class SUV(RentalVehicle):
    pass

class Truck(RentalVehicle):
    def __init__(self, make, model, rental_price_per_day, max_payload_tons):
        super().__init__(make, model, rental_price_per_day)
        self.max_payload_tons = float(max_payload_tons)

    def display_details(self):
        super().display_details()
        print(f"Max payload: {self.max_payload_tons} tons")


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact  
        self.__rentals = []

    def add_rental(self, reservation):
        self.__rentals.append(reservation)

    def update_contact(self, new_contact):
        self.__contact = new_contact

    def get_contact_masked(self):
        s = str(self.__contact)
        if "@" in s:
            name, domain = s.split("@", 1)
            return name[:1] + "***@" + domain
        if len(s) >= 7:
            return s[:3] + "****" + s[-2:]
        return "***"

    def display_rental_history(self):
        print(f"Rental history for {self.name}:")
        if not self.__rentals:
            print("  No rentals yet.")
            return
        for res in self.__rentals:
            total = res.total_cost if res.total_cost is not None else 0.0
            print(f"  - {res.vehicle.make} {res.vehicle.model} from {res.start_date} to {res.end_date} | ${total:.2f}")

    def display_details(self):
        print(f"Customer: {self.name} | Contact: {self.get_contact_masked()}")


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = None
        self.active = False

    def activate(self):
        if not self.vehicle.check_availability():
            raise RuntimeError("Vehicle is not available.")
        self.vehicle.rent()
        self.total_cost = self.vehicle.calculate_rental_cost(self.start_date, self.end_date)
        self.active = True
        self.customer.add_rental(self)

    def close(self):
        if self.active:
            self.vehicle.return_vehicle()
            self.active = False

    def display_details(self):
        total_str = f"${self.total_cost:.2f}" if self.total_cost is not None else "Pending"
        print(f"Reservation: {self.customer.name} -> {self.vehicle.make} {self.vehicle.model} | " f"{self.start_date} to {self.end_date} | Total: {total_str} | Active: {self.active}")


def show_details(entity):
    entity.display_details()


car = Car("Toyota", "Corolla", 45)
suv = SUV("Honda", "BR-V", 65)
truck = Truck("KIA", "Sportage", 80, 1.5)

show_details(car)
show_details(suv)
show_details(truck)

cust = Customer("Baqar", "k240006@nu.edu.pk")
cust.display_details()

start = date(2025, 10, 7)
end = date(2025, 10, 10)
res = RentalReservation(cust, suv, start, end)

show_details(res)  
res.activate()     
show_details(suv) 
show_details(res)  

res.close()        
show_details(suv)  
cust.display_rental_history()