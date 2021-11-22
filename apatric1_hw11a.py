#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 10: Task:
 Write a program that estimates the number of unique words in the text
 /users/abrick/resources/urantia.txt.
Extra: Command line switch that shows all filters used to find uniques
"""
# Use random for randint, use regex to filter number items.
import random
import re

# Exit gracefully if file can not be opened.
fhand = None
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()

# Declare 'constant' for how many random numbers to pick.
SELECT = 10

# Set to collect unique filtered words with len>10.
filter_set = set()

# List to collect & print the randomly chosen words
chosen_lst = list()

# Process text file per line, split potential words on space.
for line in fhand:
    words = line.split()
    for item in words:
        # Skip numbers and double hyphens.
        if re.search("[0-9]", item):
            continue
        if '--' in item:
            continue
        # Remove start punctuation, while handles multiples.
        while item.startswith(('(', '"', '-', '`')):
            item = item[1:]
        # Catches odd pattern of single end quotes closing backticks
        if item.endswith((".'", ",'", "!'", "?'")):
            item = item[:-2]
        # Remove standard end punctuation, while handles multiples.
        while item.endswith(('.', ',', ';', ':', '!', '"', ')', '-', '?')):
            item = item[:-1]
        # Check item length, add to set if > 10.
        if len(item) > 10:
            filter_set.add(item.lower())

# Create list version of filter_set for indexing
filter_lst = list(filter_set)

# Choose random words by index number, add to chosen_lst
for pick in range(SELECT):
    number = random.randint(1, len(filter_lst))
    chosen_lst.append(filter_lst[number])

# Show required results.
print(f"There are {(len(filter_set)):,} unique words with over 10 letters.")
for this in range(SELECT):
    print(chosen_lst[this])
