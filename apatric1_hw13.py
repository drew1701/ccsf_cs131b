#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 13: Task:
 Write a program that defines and demonstrates a class of book objects
 having >= 3 functions useful for handling the text content of books
"""


class Book:
    def __init__(self, filename="urantia.txt"):
        self.filename = filename
        self.sample_lines_lst = None
        try:
            with open(filename) as fhand:
                self.orig_text = fhand.read()
        except IOError:
            print('File can not be opened.')
            exit()

    def show_sample(self, linecount=25):
        # positive linecount shows begining, negative shows ending
        if linecount >= 0:
            self.sample_lines_lst = self.orig_text.splitlines()[:linecount]
            print('\nSampling', linecount, 'lines from the begining of file:')
        else:
            self.sample_lines_lst = self.orig_text.splitlines()[linecount:]
            print('\nSampling', -linecount, 'lines from the ending of file:')

        print(self.filename, '\n')
        for line in self.sample_lines_lst:
            print(line)


urantia = Book()
# print(urantia.show_sample(25))
urantia.show_sample(100)
