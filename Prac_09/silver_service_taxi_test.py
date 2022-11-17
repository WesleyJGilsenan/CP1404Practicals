"""
CP1404/CP5632 Practical
Silver Service Taxi - Wesley Gilsenan
"""

from Prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_shiny_taxi = SilverServiceTaxi("Shiny New Taxi", 100, 2)
    my_shiny_taxi.drive(18)
    print(my_shiny_taxi)
    print(my_shiny_taxi.get_fare())


main()
