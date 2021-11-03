#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 05: Task:
 Write a program that prints out the command line arguments
 it receives, in reverse order from last to first.
"""
# This test uses string methods, no loops (shorter, faster?)
# using sys.argv to access command line arguments
import sys
# pop 0 from sys.argv then join reversed
arguments = sys.argv
arguments.pop(0)
print(' '.join(reversed(arguments)))
