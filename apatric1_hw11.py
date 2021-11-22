#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 11: Task:
 Write a program that shows ten unique random words,
 all over ten characters long, that occur in the text
 /users/abrick/resources/urantia.txt
"""
# Use random for randint, use regex to filter number items.
import random
import re

# Declare constant for number of random selections
SELECT = 10

# Exit gracefully if file can not be opened.
fhand = None
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()


def find_unique_words(filehandler):
    filter_set = set()
    # Process text file per line, split potential words on space.
    for line in filehandler:
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
    return filter_set


def pick_rnd_list(howmany):
    chosen_lst = list()
    # Choose random words by index number, add to chosen_lst
    for pick in range(howmany):
        number = random.randint(1, len(filter_lst))
        chosen_lst.append(filter_lst[number])
    return chosen_lst


# Convert the return of the function into a list for indexing
filter_lst = list(find_unique_words(fhand))

# SELECT is number of picks, range is length of filter list
rand_words = pick_rnd_list(SELECT)

# Show required results.
print(f"\nThe file 'urantia.txt' has roughly {(len(filter_lst)):,}")
print("unique words with more than ten characters.")
print("Here are", SELECT, "of them, chosen at random:")
for this in range(SELECT):
    print(rand_words[this])
print()
