"""CP1404: Prac 2 Password Stars | Wesley Gilsenan"""

def main():
    password = get_password()
    generate_password(password)


def get_password():
    user_password = input("Enter Password: ")
    minimum_password_length = 3
    if len(user_password) < minimum_password_length:
        print("Not long enough")
        user_password = input("Enter Password: ")
    return user_password


def generate_password(password):
    print('*' * len(password))


main()
