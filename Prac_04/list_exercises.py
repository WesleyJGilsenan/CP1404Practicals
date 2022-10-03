"""CP1404: Prac 4 Lists Exercises | Wesley Gilsenan"""

numbers = []

for i in range(5):
    number = int(input("Please enter a number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {(sum(numbers))/5}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Please enter your username: ")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")
