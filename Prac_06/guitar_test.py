"""
CP1404: Prac 6 Guitar Test | Wesley Gilsenan

"""

from Prac_06.guitar import Guitar


def main():
    guitar_name = "Gibson L-5 CES"
    guitar_year = 1922
    guitar_cost = 16035.40

    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    print(guitar)
    print(guitar.is_vintage())


main()
