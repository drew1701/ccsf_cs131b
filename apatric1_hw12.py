#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 12: Task:
 Write a program that indicates the single greatest integer in
 /users/abrick/resources/urantia.txt
postFix: added PATH
"""
# Use regex to filter number items.
import re

# Update path at deployment.
PATH = 'urantia.txt'

# Set largest_int variable to 1 for comparison
largest_int = int(1)

# Exit gracefully if file can not be opened.
fhand = None
try:
    fhand = open(PATH)
except IOError:
    print('File can not be opened.')
    exit()

# Process text file per line: filter, trim, cast, compare.
for line in fhand:
    words = line.split()
    for item in words:

        # Skip if no numerics at all.
        if not re.search(r'\d', item):
            continue
        # Skip numerics with not digits in middle, leave commas
        if re.search(r'\d+[^\d,]+\d+', item):
            continue

        # Remove leading not digits.
        while re.search(r'^\D', item):
            item = item[1:]
        # Remove trailing not digits.
        while re.search(r'\D$', item):
            item = item[:-1]
        # Remove commas from formatted large numbers.
        item = re.sub(",", "", item)

        # Carefully cast str to int, if error skip item.
        try:
            item_int = int(item)
        except ValueError:
            continue

        # Compare current item to largest_int, keep greater value.
        if item_int > largest_int:
            largest_int = item_int

# Show required results.
print(f"\nThe largest integer found in the file 'urantia.txt' is:")
print(f"{largest_int :,}\n")
