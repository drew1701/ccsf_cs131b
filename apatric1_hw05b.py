#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 05: Task:
 Write a program that prints out the command line arguments it receives,
 in reverse order from last to first.
"""
# This alternate uses function with *args

def lifo(*args):
    index = len(args) - 1
    while index >= 0:
        print(args[index])
        index -= 1


lifo('one', 'two', 'three')
lifo(1, 2, 3, 4)
lifo()
lifo(69, 'mixed', 99)
