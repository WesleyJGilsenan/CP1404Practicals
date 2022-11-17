"""
CP1404/CP5632 Practical - Unreliable Car.py Wesley Gilsenan

"""

from Prac_09.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_num = randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

