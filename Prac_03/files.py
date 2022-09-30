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


# Program 3 - Open numbers and add the first two numbers
number_file = open('numbers.txt', 'r')
number_1 = int(number_file.readline())
number_2 = int(number_file.readline())
sum_of_numbers = (number_1 + number_2)
print(sum_of_numbers)
number_file.close()


# Program 4 - Opens numbers.txt for any number of numbers
number_file = open('numbers.txt', 'r')
sum_of_numbers = 0
for line in number_file:
    number = int(line)
    sum_of_numbers = sum_of_numbers + number
print(sum_of_numbers)
number_file.close()
