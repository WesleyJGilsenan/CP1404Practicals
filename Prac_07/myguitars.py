"""
CP1404/CP5632 Practical 07 - My Guitars Wesley Gilsenan
"""

FILENAME = "guitars.csv"
from guitar import Guitar


def main():
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        line = line.strip()
        parts = line.split(",")
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitars.append(parts)
        print(Guitar(guitars))
    in_file.close()


main()