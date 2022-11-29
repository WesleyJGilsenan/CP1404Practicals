"""Prac 10 wiki - Wesley Gilsenan"""

import wikipedia


user_input = input("Please enter your search: ")
while user_input != '':
    try:
        print(wikipedia.search(user_input))
        current_page = wikipedia.page(user_input, auto_suggest=False)
        print(current_page.title)
        print(wikipedia.summary(user_input))
        print(current_page.url)
    except wikipedia.exceptions.DisambiguationError:
        print("error")
    user_input = input("Please enter your search: ")
