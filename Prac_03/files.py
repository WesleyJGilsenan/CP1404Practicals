""" CP1404: Prac 3 Files | Wesley Gilsenan """

# Program 1 - Record user name into name.txt
user_name = input("Please input your name: ")
user_file = open("name.txt", 'w')
print(user_name, file=user_file)
user_file.close()


# Program 2 - Open file and read name
user_file = open("name.txt", 'r')
for name in user_file:
    print(f"Your name is {name}")
user_file.close()

