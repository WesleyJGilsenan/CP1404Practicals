def main():
    menu = """G - Get Score
P - Print result
S - Print stars
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            user_score = get_score()
            print(menu)
            choice = input(">>> ").upper()
        elif choice == "P":
            print(f"Your score is {user_score:.0f}")
            print(menu)
            choice = input(">>> ").upper()
        elif choice == "S":
            print_stars(user_score)
            print(menu)
            choice = input(">>> ").upper()
        else:
            print("Invalid input")
            print(menu)
            choice = input(">>> ").upper()
    print("Thank you.")


def get_score():
    check_score = float(input("Please input a score between 0 to 100: "))
    while check_score not in range(0, 100):
        print("invalid Input")
        check_score = float(input("Please input a score between 0 to 100: "))

    return check_score


def print_stars(score):
    score = int(score)
    print('*' * score)

main()
