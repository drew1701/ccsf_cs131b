#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 09: Task:
 Write a program that prints the sum of all the integer arguments
 passed, ignoring any non-integer arguments that may be mixed in.
"""
import sys

# Set a variable to collect sum of integer arguments.
sum_args = 0

# Try converting arg to int and adding to sum, skip if error.
for arg in sys.argv[1:]:
    try:
        sum_args += int(arg)
    except ValueError:
        continue

# Output formatted results.
print(f'\nThe sum of the integer command line arguments is {sum_args:,}.\n')
