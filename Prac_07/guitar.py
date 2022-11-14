"""
CP1404/CP5632 Practical 07 - Guitar Class Wesley Gilsenan
"""


class Guitar:

    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"{self.name} {self.year} {self.cost}"

    def __lt__(self, other):
        return self.year < other.year
