#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 007: Task:
 Write a program that simulates the throwing of a 9-sided die and a
 9000-sided die, indicating whether or not the sum of the results
 is a multiple of three.
"""
import random
# set a random number for each die, add dice
d9 = random.randint(1, 9)
d9k = random.randint(1, 9000)
dice_sum = d9 + d9k
# set divby3 to yes if dice_sum is a multiple of 3
if dice_sum % 3 == 0:
    divby3 = 'Yes'
else:
    divby3 = 'No'
# Output dice rolls and results
print('\nOne roll of a 9 sided die equals ' + str(d9) + '.')
print('One roll of a 9000 sided die equals ' + str(d9k) + '.')
print('The combined total is ' + str(dice_sum) + '.')
print('Is ' + str(dice_sum) + ' a multiple of 3? ' + divby3 + '.\n')
