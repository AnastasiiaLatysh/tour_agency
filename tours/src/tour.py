from abc import ABC


class Tour(ABC):

    def __init__(self, nname, pprice, aavailable_seats, ccountry, ccity):
        self.name = nname
        self.price = pprice
        self.available_seats = aavailable_seats
        self.country = ccountry
        self.city = ccity
        self.vehicle_model = None

    def __str__(self):
        return f"Tour '{self.name}': price - {self.price}, country - {self.country}," \
            f" city - {self.city}, available_seats - {self.available_seats}"

    def add_vehicle_model(self):
        print("Enter vehicle model:\n")
        self.vehicle_model = input()

    def update_price(self):
        print("Enter new price:\n")
        self.price = input()
