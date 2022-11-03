"""
CP1404: Prac 6 Language| Wesley Gilsenan

"""

from Prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)

    programing_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programing_languages:
        if language.is_dynamic():
            print(language.name)


main()
