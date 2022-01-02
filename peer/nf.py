'''
TASK-- 
Write a program that defines and demonstrates a class of book objects having 
at least three functions useful for handling the text content of books 
'''

fhand = "urantia.txt"
#test1 = "num_test.txt"
class book:
    '''
    book object 1: Book File Name
    '''
    def __init__(self,title):
        self.open = open(title)
        print('\n',
        "This book's file name is: ",
        title, #,self
        '\n')

    '''
    book object 2: Trimmed and word count
    '''
    def trim(self):
        trimmed = set()
        for line in self.open:
            line = line.strip().lower() #strips whitespaces & lower case all
            '''remove interesting punctuations from lines'''
            punc = '''`!()--[]}{;:"\,<>./?@#$%^&*_~''' #assign punctuations to remove.
            for punctuation in line:
                if punctuation in punc:
                    line = line.replace(punctuation, "") #replacing punctuations with blank: For words with hyphens, they'll be considered as individual words.
            # print (line) #<-this prints out lines without punctuation.
            '''split lines into words and remove digit words; append all unique(single) words to empty set'''
            for words in line.split():
                if words.isdigit():continue #filter out digit words
                trimmed.add(words) #adds the trimmed words to the set for unique listing
            #print(words,len(words)) #prints words without digits
        """function's print statement marker"""
        print (
            "Trimmed: \n","This book's text content has {} words.".format(len(trimmed))
            )
        return trimmed, #return value for patching


    '''
    book object 3: number counts
    '''
    def nums(self):
        num = 0
        num_bin = []
        for line in self.open:
            line = line.strip().lower() #strips whitespaces & lower case all
            '''remove interesting punctuations from lines'''
            punc = '''`!()--[]}{;:"\,<>./?@#$%^&*_~''' #assign punctuations to remove.
            for punctuation in line:
                if punctuation in punc:
                    line = line.replace(punctuation, "") #replacing punctuations with blank: For words with hyphens, they'll be considered as individual words.
            # print (line) #<-this prints out lines without punctuation.
            '''split lines into words and remove digit words; append all unique(single) words to empty set'''
            for words in line.split():
                if words.isdigit():
                    num += 1
                    num_bin.append(words) #filter out digit words
                # trimmed.add(words) #adds the trimmed words to the set for unique listing 
        print("number count:\n", "Its content has,", num, "numbers in it"#,num_bin
            )
        return num_bin #return value for future patching


'''unhash to view the book class'''
f = book(fhand)
f.nums()
f.trim() #i'm unsure why this output get's influenced by the previous call when un hashed
#f
#n = book(test1)
#n
#n.trim()
#n.nums()#same for this call.
