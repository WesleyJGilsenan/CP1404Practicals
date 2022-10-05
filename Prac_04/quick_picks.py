"""CP1404: Prac 4 Quick Picks | Wesley Gilsenan"""

import random

MINIMUM = 1
MAXIMUM = 45
PICKS_PER_LINE = 6


def main():
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        picks = []
        for k in range(PICKS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            picks.append(number)
        picks.sort()
        print(f"{picks[0]:2} {picks[1]:2} {picks[2]:2} {picks[3]:2} {picks[4]:2} {picks[5]:2}")


main()
