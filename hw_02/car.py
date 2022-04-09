"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw_02.base import Vehicle
from hw_02.engine import Engine

class Car(Vehicle):
    def __init__(self, engine):
        self.engine = engine

    def set_engine(self):
        self.engine = Engine
