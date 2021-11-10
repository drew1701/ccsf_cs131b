#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 10: Task:
 Write a program that estimates the number of unique words in the text
 /users/abrick/resources/urantia.txt.
"""
# Use regex to filter number items.
import re

# Use argv to watch for command line switches
import sys

# Exit gracefully if file can not be opened.
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()

# Use set to collect filtered unique words only.
filter_set = set()

# Variables to count the filtered (non word) items.
item_count = 0
num_count = 0
dash_count = 0
nofilter_set = set()

for line in fhand:
    words = line.split()
    for item in words:
        item_count += 1
        nofilter_set.add(item.lower())
        # Skip past non words.
        if re.search("[0-9]", item):
            num_count += 1
            continue
        if '--' in item:
            dash_count += 1
            continue
        # Add item in lower case after removing end punctuation.
        if item.endswith((".", ",", ";", ":", "!")):
            filter_set.add(item.lower()[:-1])
        else:
            filter_set.add(item.lower())

punct_dif = len(nofilter_set) - len(filter_set) - num_count - dash_count

# Show required results.
print("\nIf spaces are used to deliminate words and any character(s)")
print(f"can be called a word, there are a total of {item_count:,}")
print(f"words in the file 'urantia.txt'. {(len(nofilter_set)):,} are unique.")
print("\nIf non-words like numbers and punctuation are filtered from")
print(f"the results, there are closer to {(len(filter_set)):,} unique words.")


'''
print(f"\nThe file 'urantia.txt' contains roughly {(len(filtered_set)):,}"
      f" unique words.")
print(f"There were a total of {item_count:,} potential words identified.")
'''
# Show all work if '-a' argument found on command line.
if len(sys.argv) > 1 and sys.argv[1].lower() == "-a":
    print(f"\n{num_count:,} number items like '0:0.1' removed as not words")
    print(f"{dash_count:,} double dashes '--' removed as not words")
    print(f"{punct_dif:,} words ending with punctuation like 'word.'"
          f" removed as not unique\n")
else:
    # Show user the command line option.
    print("\nUse '-a' on the command line to show all filters applied.\n")
