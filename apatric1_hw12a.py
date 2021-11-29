#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 12a: Task:
 Write a program that indicates the single greatest integer in
 /users/abrick/resources/urantia.txt
NOTE: rough code
Actual largest integer: 842,842,682,846,782
"""
# Use regex to filter number items.
import re

# Set largest_int variable to 1 for comparison
largest_int = int(1)

# Exit gracefully if file can not be opened.
fhand = None
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()

# Process text file per line, filter then compare str values
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
        # Remove commas from formatted large numbers
        item = re.sub(",", "", item)

        # Carefully convert str to int, non digits should be filtered
        try:
            item_int = int(item)
        except ValueError:
            continue

        # Compare current item to largest, keep largest
        if item_int > largest_int:
            largest_int = item_int

print(f"big one {(largest_int):,}")

# Show required results.
#print(f"\nThe file 'urantia.txt' has roughly {(len(filter_lst)):,}")
#print("unique words with more than ten characters.")

