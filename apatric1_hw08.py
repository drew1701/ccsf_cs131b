#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 08: Task:
 Adapt the previous assignment to roll both dies one hundred times,
 indicate how many times the sum of the results was a multiple of three.
"""
import random
# set variable to count dice roll sums that are divisible by 3
divby3 = 0
# loop to roll each die 100 times, if sum is multiple of 3 increment
for roll in range(100):
    if (random.randint(1, 9) + random.randint(1, 9000)) % 3 == 0:
        divby3 += 1
# Output results
print('\nAfter rolling one 9 sided die and one 9000 sided die')
print('one hundred times, the sum of the two dice was a')
print('multiple of three exactly ' + str(divby3) + ' times.\n')
