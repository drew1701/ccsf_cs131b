#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 05: Task:
 Write a program that prints out the command line arguments
 it receives, in reverse order from last to first.
"""
# using sys.argv to access command line arguments
import sys
# set index to last item
index = len(sys.argv) - 1
# loop list last to first, skip 0, output on same line
while index > 1:
    print(sys.argv[index], end=' ')
    index -= 1
# at final argument end with standard new line
if index == 1:
    print(sys.argv[index])
