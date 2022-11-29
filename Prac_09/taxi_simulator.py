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
    user_taxi = None
    total_cost = 0
    print(MENU)
    user_selection = input(">>> ").lower()
    while user_selection != 'q':
        if user_selection == 'c':
            print("Taxis avaliable:")
            taxi_selection(taxis)
            user_choice = int(input("Choose taxi: "))
            try:
                user_taxi = taxis[user_choice]
            except IndexError:
                print("Invalid taxi choice")
            print(MENU)
            user_selection = input(">>>").lower()
        elif user_selection == 'd':
            if user_taxi:
                user_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                user_taxi.drive(distance_to_drive)
                trip_cost = user_taxi.get_fare()
                print(f" {user_taxi.name} trip cost you ${trip_cost}")
                total_cost += trip_cost
                print(f"Bill to date: ${total_cost}")
            print(MENU)
            user_selection = input(">>>").lower()
        else:
            print("Invalid option")
            print(MENU)
            user_selection = input(">>>").lower()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    taxi_selection(taxis)


def taxi_selection(taxis):
    for counter, taxi in enumerate(taxis):
        print(f"{counter} - {taxi}")


main()
