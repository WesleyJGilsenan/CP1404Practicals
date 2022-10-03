"""CP1404: Prac 4 Lists warmup | Wesley Gilsenan"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 1 (wrong it was 2)
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
numbers = numbers[2:]
print(numbers)
print(9 in numbers)

