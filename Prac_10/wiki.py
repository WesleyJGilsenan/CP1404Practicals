"""Prac 10 wiki - Wesley Gilsenan"""

import wikipedia


user_input = input("Please enter your search: ")
while user_input != '':
    print(wikipedia.search(user_input))
    print(wikipedia.summary(user_input))
    user_input = input("Please enter your search: ")
