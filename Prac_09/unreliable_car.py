"""
CP1404/CP5632 Practical - Unreliable Car.py Wesley Gilsenan

"""

from Prac_09.car import Car


class Unreliable(Car):

    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability



