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

# Exit gracefully if file can not be opened.
try:
    fhand = open('urantia.txt')
except Exception:
    print('file cannot be opened')
    exit()

# Use set to collect unique words only.
unique_words = set()

# Variables to count the skipped (non word) items.
skipnum = 0
skipdash = 0
endpunctcnt = 0
endpunctset = set()
allitemcount = 0

for line in fhand:
    words = line.split()
    for item in words:
        allitemcount += 1
        # Skip past non words.
        if re.search("[0-9]", item):
            skipnum += 1
            continue
        if '--' in item:
            skipdash += 1
            continue
        # Add item in lower case after removing end punctuation.
        if item.endswith((".", ",", ";", ":", "!")):
            endpunctcnt += 1
            endpunctset.add(item.lower())
            unique_words.add(item.lower()[:-1])
        else:
            unique_words.add(item.lower())

# Show results, show filtered items.
print("Unique", len(unique_words))
print("skipnum", skipnum)
print("skipdash", skipdash)
print("endpunctcount", endpunctcnt)
print("uniqueEndPunct", len(endpunctset))
print("AllItems", allitemcount)
