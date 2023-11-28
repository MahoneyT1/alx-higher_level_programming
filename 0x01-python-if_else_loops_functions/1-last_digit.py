#!/usr/bin/python3
import random

# assign a variable to hold the generated random number

number = random.randint(-1000, 1000)

#check if number is the last digit of the total number

last_digit_of_a_number = abs(number) % 10

#check if the last digit is greater than 5

if last_digit_of_a_number > 5:
    print(f'Last digit of {number} is {last_digit_of_a_number} and is greater than 5')

elif last_digit_of_a_number == 0:
    print(f'Last digit of {number} is {last_digit_of_a_number} and is zero')

elif last_digit_of_a_number < 6 and not last_digit_of_a_number == 0:
        print(f'Last digit of {number} is {last_digit_of_a_number} and is less than 6 and not 0')
