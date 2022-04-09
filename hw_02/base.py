from abc import ABC
from hw_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = None
    fuel = None
    fuel_consumption = None
    started = "Not started"

    def __init__(self, weight, fuel, fuel_consumption, started):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started == "Not started":
            if self.fuel > 0:
                self.started = "started"
            else:
                raise LowFuelError

    def move(self):
        if self.fuel - self.fuel_consumption*input("Ввeдите дистанцию") <= 0:
            raise NotEnoughFuel
        else:
            self.fuel = self.fuel - self.fuel_consumption*input("Ввeдите дистанцию")
