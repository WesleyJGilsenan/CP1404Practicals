"""
CP1404/CP5632 Practical
My Taxi - Wesley Gilsenan
"""

from Prac_09.Taxi import Taxi


def main():
    print("my taxi")
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
