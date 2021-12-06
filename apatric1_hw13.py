#!/usr/bin/env python3
"""
Andrew Patrick - apatric1
Prog Fundamentals: Python
Homework 13: Task:
 Write a program that defines and demonstrates a class of book objects
 having >= 3 functions useful for handling the text content of books
"""
import random


class Book:
    def __init__(self, filename="urantia.txt"):
        self.filename = filename
        self.sample_lines_lst = list()
        self.chosen_lst = list()
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

    def find_largest_int(self):
        import re
        largest_int = 0
        words = self.orig_text.split()
        for item in words:
            # Skip if no numerics at all.
            if not re.search(r'\d', item):
                continue
            # Skip numerics with not digits in middle, leave commas
            if re.search(r'\d+[^\d,]+\d+', item):
                continue

            # Remove leading not digits.
            while re.search(r'^\D', item):
                item = item[1:]
            # Remove trailing not digits.
            while re.search(r'\D$', item):
                item = item[:-1]
            # Remove commas from formatted large numbers.
            item = re.sub(",", "", item)

            # Carefully cast str to int, if error skip item.
            try:
                item_int = int(item)
            except ValueError:
                continue

            # Compare current item to largest_int, keep greater value.
            if item_int > largest_int:
                largest_int = item_int

        print("\nThe largest integer in the file", self.filename, 'is:')
        print(f"{largest_int :,}")

    def pick_unique_words(self, howmany=10):
        import re
        filter_set = set()
        words = self.orig_text.split()
        for item in words:
            # Skip numbers and double hyphens.
            if re.search("[0-9]|[--]", item):
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
            if len(item) > 0:
                filter_set.add(item.lower())

        filter_lst = list(filter_set)
        for pick in range(howmany):
            number = random.randint(1, len(filter_lst))
            self.chosen_lst.append(filter_lst[number])

        print('\nHere are', howmany, 'unique words from the file:')
        print(self.filename, '\n')
        for word in self.chosen_lst:
            print(word)

# Create instance of Book class named urantia
urantia = Book()

# Demonstrate the functions
urantia.show_sample(13)
urantia.find_largest_int()
urantia.pick_unique_words(7)
