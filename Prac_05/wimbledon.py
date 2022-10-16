"""
CP1404: Prac 5 Wimbledon | Wesley Gilsenan
"""

FILENAME = 'wimbledon.csv'
COUNTRY = 1
CHAMPION = 2


def main():
    records = generate_information()
    champions, countries = arrange_champions(records)
    display_champions(champions, countries)


def generate_information():
    champion_information = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            section = line.strip().split(",")
            champion_information.append(section)
    return champion_information


def arrange_champions(records):
    champions = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
        try:
            champions[record[CHAMPION]] += 1
        except KeyError:
            champions[record[CHAMPION]] = 1
    return champions, countries


def display_champions(champions, countries):
    print("Wimbledon Champions: ")
    for name, count in champions.items():
        print(name, count)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
