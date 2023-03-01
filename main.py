import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

        def __init__(self, name="Human"):
            self.name = name
            nick = Human("Nick")
            kate = Human("Kate")
            car = Auto("TopAz")
            car.add_passenger(nick)
            car.add_passenger(kate)
            car.print_passengers_names()

        def __init__(self, name="Human",
                     job=None, home=None,
                     car=None):
            self.name = name
            self.money = 100
            self.gladness = 50
            self.satiety = 50
            self.job = job
            self.car = car
            self.home = home

        def add_passenger(self, human):
            self.passenger.append(human)

            def print_passengers_names(self):
                if self.passengers != []:
                    print(f"Names of{self.brand}passengers:")
                    for passengers in self.passengers:
                        print(passengers.name)
                else:
                        print(f"There are no passengers) in{self.brand}")

