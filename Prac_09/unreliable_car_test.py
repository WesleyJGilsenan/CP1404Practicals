"""
CP1404/CP5632 Practical
My Unreliable Car - Wesley Gilsenan
"""

from Prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Half broken 4x4", 100, 50)
    my_car.drive(40)
    print(my_car)
    my_car.drive(10)
    print(my_car)
    my_car.drive(80)
    print(my_car)


main()
