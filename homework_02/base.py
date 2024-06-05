from abc import ABC
import exceptions


class Vehicle(ABC):
    def __init__(self, weight=10, fuel=100, fuel_consumption=1):
        self.started: bool = False
        self.weight: int = weight
        self.fuel: int = fuel
        self.fuel_consumption: int = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else: raise exceptions.LowFuelError()

    def move(self, distance):
        fuel_cost = distance * self.fuel_consumption
        if fuel_cost < self.fuel:
            self.fuel -= fuel_cost
        else: raise exceptions.NotEnoughFuel()
