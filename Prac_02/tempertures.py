"""CP1404: Prac 2 Tempertures | Wesley Gilsenan"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
            choice = input(">>> ").upper()
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
            choice = input(">>> ").upper()
        else:
            print("Invalid option")
            print(menu)
            choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
