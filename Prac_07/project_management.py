"""
CP1404: Prac 7 Project Management | Wesley Gilsenan

Estimated time to complete: 1 and a half hours
Actual time:
"""


from Prac_07.project import Project


def main():
    menu_input = main_menu()
    while menu_input.upper() != "Q":
        if menu_input.upper() == "L":
            load_project()
            menu_input = main_menu()
        elif menu_input.upper() == "S":
            save_project()
            menu_input = main_menu()
        elif menu_input.upper() == "D":
            display_project()
            menu_input = main_menu()
        elif menu_input.upper() == "F":
            filter_project()
            menu_input = main_menu()
        elif menu_input.upper() == "A":
            add_project()
            menu_input = main_menu()
        elif menu_input.upper() == "U":
            update_project()
            menu_input = main_menu()
        else:
            print("Invalid input")
            menu_input = main_menu()
    print("Thank you for using custom-built project management software.")


def main_menu():
    user_input = input("""
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> """)
    return user_input


def load_project():
    print("load project")


def save_project():
    print("save project")


def display_project():
    print("display project")


def filter_project():
    print("Filter Project")


def add_project():
    print("add project")


def update_project():
    print("update project")


main()
