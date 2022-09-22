import random

"""CP1404: Prac 2 Score | Wesley Gilsenan"""


def main():
    user_score = float(input("Enter score: "))
    print(check_score(user_score))
    ran_user_score = random.randint(1, 100)
    print(ran_user_score)
    print(check_score(ran_user_score))


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


main()

