"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine: Engine = None

    def set_engine(self, eng: Engine):
        self.engine = eng
