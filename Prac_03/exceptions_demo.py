""" CP1404: Prac 3 exceptions_demo | Wesley Gilsenan

CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? It will occur when the user inputs anything other than a number.
2. When will a ZeroDivisionError occur? This will occur when the user inputs a 0 to the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, use a while loop as I have below to check if denominator has been entered as a 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Error 0 can not be divided.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
    # print("Cannot divide by zero!")
print("Finished.")