"""
CP1404: Prac 5 Wimbledon | Wesley Gilsenan
"""

FILENAME = 'wimbledon.csv'


def main():
    print("memes")
    records = generate_information()
    print(records)


def generate_information():
    champion_information = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            section = line.strip().split(",")
            champion_information.append(section)
    return champion_information


# def arrange_champions():


# def display_champions():


main()
