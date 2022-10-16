"""
CP1404: Prac 5 Emails | Wesley Gilsenan

Estimate: 30 minutes
Actual:   64 minutes


"""


def main():
    user_database = {}
    new_user = input("Email: ")
    while new_user != "":
        new_user_name = extract_name(new_user)
        user_check = input(f"is your name {new_user_name}? (Y/n)")
        if user_check.lower() == "y":
            user_database[new_user] = new_user_name
            new_user = input("Email: ")
        else:
            new_user = input("Email: ")
    for new_user, new_user_name in user_database.items():
        print(f"{new_user} {new_user_name}")


def extract_name(email):
    name = email.split('@')[0]
    return name


main()

