#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 10: Task:
 Write a program that estimates the number of unique words in the text
 /users/abrick/resources/urantia.txt.
Extra: Command line switch that shows all filters used to find uniques
"""
# Use regex to filter number items.
import re

# Use argv to watch for command line switches
import sys

# Exit gracefully if file can not be opened.
fhand = None
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()

# Use set to collect filtered unique words only.
filter_set = set()

# Variables to count all and filtered items.
item_count = 0
num_count = 0
p_count = 0
nofilter_set = set()
punct_set = set()

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
            continue
        # Add item in lower case after removing end punctuation.
        if item.endswith((".", ",", ";", ":", "!")):
            filter_set.add(item.lower()[:-1])
        else:
            filter_set.add(item.lower())

filter_dif = len(nofilter_set) - len(filter_set)
punct_dif = filter_dif - num_count - 1

# Show required results.
print("\nIf spaces are used to deliminate words and any character(s)")
print(f"can be called a word, there are a total of {item_count:,}")
print(f"words in the file 'urantia.txt'. {(len(nofilter_set)):,} are unique.")
print("\nIf non-words like numbers and punctuation are filtered from")
print(f"the results, there are closer to {(len(filter_set)):,} unique words.")

# Show all work if '-a' argument found on command line.
if len(sys.argv) > 1 and sys.argv[1].lower() == "-a":
    print("\nTotal unique items removed by each filter type:")
    print(f"{num_count:,} number items like '0:0.1' removed as not words.")
    print(f"{punct_dif:,} words ending with punctuation like 'word.'"
          f" removed as not unique.")
    print("     1 double dash '--' removed as not a word.")
    print(f"{filter_dif:,} total unique word items filtered.\n")
else:
    # Show user the command line option.
    print("\nUse '-a' on the command line to show all filters applied.\n")
