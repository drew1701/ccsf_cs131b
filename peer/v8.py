# CS 131B Week 14 assignment
# 11/29 - 12/5/21
# Write a program that defines and demonstrates a class of book objects having at least three functions useful for handling the text content of books

'''
Defines the class called "Book"
defines the initiator, and with arguments name, book format, Total unique words, and the greatest number
function to print the name of the book that is an object of the class Book
function to prin the digital format of the book
function to find the total # of words from the object = Urantia.txt
function to print the greatest integer from a list of integers from the book object Urantia
runs the function bookname for object B1 that's part of the class "Book".
runs the function bkformat that's part of the class "Book".
runs the function uniq_words for object B1 that's part of the class "Book".
runs the function highnum for object B1 that's part of the class "Book".
'''

class Book:
	def __init__(self,name,bkformat,unique_words,highnum):
		self.name = name
		self.bkformat = "digital"
		self.TtlUnique_words = unique_words
		self.highnum = highnum

	def bookname(self):
		print("The following content info is from the Urantia book object that is part of the Book Class.")
#	bookname(self)

	def bkformat(self):
		print("The format of the book is in digital format")
#	bkformat(self)

	def uniq_words(self):
		file = open("/users/abrick/resources/urantia.txt", "r")
		data = (file.read()).lower()
		words = set(data.split())
		uniq_words = list()
		for word in words:
			if word.isalpha():
				uniq_words.append(word)
		print('Total Unique Words:', len(uniq_words))
#	uniq_words(self)

	import re
	def highnum(self):
		file = open("/users/abrick/resources/urantia.txt", "r")
		data = (file.read()).lower()
		numbers = set(re.findall(r'\d+',data))
		highnum = max(numbers)
		print("The highest number is: ",highnum,".")
#	highnum(self)

B1 = Book("one", "two", "three", "four")
#B1.bookname(self)
#B1.bkformat(self)
#B1.uniq_words(self)
#B1.highnum(self)
