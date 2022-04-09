"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_02.base import Vehicle
from hw_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo, weight, fuel, fuel_consumption, started):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self):
        if (self.cargo + input("Вес груза: ")) < self.max_cargo:
            self.cargo = self.cargo + input("Вес груза: ")
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        print(f"Вес до обнуления {self.cargo}")
        self.cargo = 0
