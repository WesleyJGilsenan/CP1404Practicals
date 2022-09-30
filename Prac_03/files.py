""" CP1404: Prac 3 Files | Wesley Gilsenan """

# Program 1 - Record user name into name.txt
user_name = input("Please input your name: ")
user_file = open("name.txt", 'w')
print(user_name, file=user_file)
user_file.close()


