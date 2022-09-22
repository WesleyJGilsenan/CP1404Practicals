"""CP1404: Prac 1 Menus | Wesley Gilsenan"""

user_name = input("Enter Name: ")
menu = ("""
(H)ello
(G)oodbye
(Q)uit
""")
print(menu)
user_input = input(">>>").upper()
while user_input != "Q":
    if user_input == "H":
        print(f"Hello {user_name}")
    elif user_input == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print(menu)
    user_input = input(">>>").upper()

print("Finished")
