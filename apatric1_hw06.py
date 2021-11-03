#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 06: Task:
 Write a program that prints in alphabetical order all
 the unique command line arguments it receives.
"""
# using sys.argv to access command line arguments
import sys
arguments = sys.argv

# remove index 0 because it isn't an argument
arguments.pop(0)

# convert list to set to remove duplicates
args_set = set(arguments)

# sort the set and print with space delimiter
print(' '.join(sorted(args_set)))
