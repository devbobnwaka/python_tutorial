import random
from pathlib import Path
from utils import find_max

# print(find_max([70, 32, 5]))
path = Path()
for file in path.glob('*.py'):
    print(file)

"""
CREATE A CLASS DICE
"""

# class Dice:
#     def __init__(self):
#         self.side = 6

#     def roll(self): 
#         side1 = random.randint(1, self.side)
#         side2 = random.randint(1, self.side)
#         return side1, side2

# dice = Dice()
# print(dice.roll())


"""
CREATE A PERSON CLASS
"""

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'Hi, I am {self.name}')


# person1 = Person('John Smith')
# person1.talk()

"""
APP THAT CONVERT PHONE NUMBERS TO WORDS
"""

# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "0": "Zero"
# }

# num_in_word = ''
# phone_number = input('Phone: ')
# for num in phone_number:
#     num_in_word += digits_mapping.get(num, "!") + " "
# print(num_in_word)

""""
Write a program to remove the duplicates in a list
"""

# numbers = [2, 3, 2, 3, 45, 2, 1, 45, 3]
# unique = []

# print(numbers.count(2))
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)



""""
WRITE A PROGRAM to find the largest number in a list
"""
# numbers = [70, 32, 5]
# largest_number = numbers[0]

# for number in numbers:
#     if number > largest_number:
#         largest_number = number

# print(f'The largest number is: {largest_number}')

"""
DRAW THE LATER F
"""
# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ''
#     for x in range(x_count):
#         output += 'x'
#     print(output)

"""
USE A FOR LOOP TO CALCULATE ALL THE PRICES
"""
# prices = [10, 20, 30]
# total_price = 0
# for price in prices:
#     total_price += price

# print(f'TOTAL PRICE: {total_price}')


"""
CAR GAME
"""
# command = ''
# started = False
# stopped = False

# while True:
#     command = input('> ').lower()

#     if command == 'help':
#         print("""start - to start the car
# stop - to stop the car
# quit - to exit
#         """)
#     elif command == 'start':
#         if started:
#             print('Car already started')
#         else:
#             started = True
#             stopped = False
#             print("Car started...Ready to go")
#     elif command == 'stop':
#         if stopped:
#             print('Car already stopped')
#         else:
#             stopped = True
#             started = False
#             print("Car stopped.")
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that...")

    


"""
APP THAT COLLECTS user input either in pounds or kg then print it converted
"""

# weight = input('Weight: ')
# unit = input('(L)bs or (K)g: ').lower()
# if unit == 'l':
#     weight_in_kg = round(int(weight)*0.454, 0)
#     print(f'You are {weight_in_kg} kilos')
# if unit == 'k':
#     weight_in_pds = round(int(weight)/0.454, 0)
#     print(f'You are {weight_in_pds} kilos')

"""
# PROGRAM TO ASK TWO QUESTIONS: PERSON'S NAME AND FAVORITE COLOR
Then, Print a message like "Bob likes blue
"""
# name = input("Whats's your name? ")
# color = input("Whats's your favorite color? ")
# print(name + ' likes ' + color)

"""
ASK as user their weight (in pounds), convert it to kilograms and print on the terminal
"""
# weight_in_pounds = input("What is your weight(lbs)? ")
# weight_in_kg = int(weight_in_pounds)/2.2046 #you can also multiply by 0.454 instead of division

# print('Your weight is ' + str(weight_in_kg) + 'kg.')

"""
PRICE OF A HOUSE IS $1M.
if buyer has good credit,
    they need to put down 10%
otherwise 
    they need to put down 20%
Print the down payment
"""

# price = 1000000
# has_good_credit = False

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')

"""
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise 
    name looks good!
"""

# name = 'Ra'

# if len(name) < 3:
#     print(f'{name}, name must be at least 3 characters')
# elif len(name) > 50:
#     print(f'{name}, name can be a maximum of 50 characters')
# else:
#     print(f'{name}, name looks good!')


