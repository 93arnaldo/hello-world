#Welcome to the Lottery numbers generator.

print Welcome to the Lottery numbers generator
Number_of_values = int(raw_input("Please enter how many random numbers would you like to have: "))

import random 

Lottery_number = []

for item in range(Number_of_values):
    item = random.randint(0, 99)
    Lottery_number.append(item)

print Lottery_number
