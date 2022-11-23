"""
CP1404/CP5632 Practical - Taxi simulator Wesley Gilsenan

"""

from Prac_06.car import Car
from Prac_09.Taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    user_selection = input(">>> ").lower()
    while user_selection != 'q':
        if user_selection == 'c':
            print("Taxis avaliable:")
            taxi_selection(taxis)
            user_taxi = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[user_taxi]
            except IndexError:
                print("Invalid taxi choice")
            print(MENU)
            user_selection = input(">>>").lower()
        elif user_selection == 'd':
            print("drive")
            print(MENU)
            user_selection = input(">>>").lower()
        else:
            print("Invalid option")
            print(MENU)
            user_selection = input(">>>").lower()
    print("Taxis are now:")


def taxi_selection(taxis):
    for counter, taxi in enumerate(taxis):
        print(f"{counter} - {taxi}")


main()
