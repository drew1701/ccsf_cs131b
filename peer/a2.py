import sys, re

class Book :
  def __init__ (self, book_name, author_name, book_size, genre):
    self.book_name = book_name
    self.author_name = author_name
    self.book_size = book_size
    self.genre = genre
    
   
  def save_content(self, book):
    self.txt = open(book, "r+")
    self.content = self.txt.read()
    
    
  
  def search(self, phrase):
    for line in self.txt:
      x = re.search(phrase, line)
      if x != None:
        return line
      else:
        return None
      
       
        
  def change (self, target, phrase):
    for line in txt:
      x = re.search(target, line)
      if x!= None:
        txt.write(line.replace(phrase, target))

        
def appendToBook (self, phrase):
  txt.write(phrase)

test = Book('one', 'two', 'three', 'four')

test.save_content('urantia.txt')
test.search("test")
test.change()
test.appendToBook()