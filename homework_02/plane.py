"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: int = 0
        self.max_cargo: int = max_cargo
        # self.weight += self.cargo
        print(self.weight, self.cargo, self.max_cargo)

    def load_cargo(self, new_cargo: int):
        if new_cargo + self.cargo <= self.max_cargo:
            self.cargo += new_cargo
            self.weight += new_cargo
        else: raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_buffer = self.cargo
        self.cargo = 0
        self.weight -= self.cargo
        return cargo_buffer
