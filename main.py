class Library:
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for books in self.books:
            print(' *'+books)

    def __init__(self,listOfBooks):
        self.books = listOfBooks
    
    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it self and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book has been already taken by someone else, please wait till it is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for return this book, hope you enjoyed reading this book.")
    
    

class Student:
    def requestBook(self):
        self.book= input("Enter the name of the book you want to borrow:")
        return self.book

    def returnBook(self):
        self.book= input("Enter the name of the book you want to return:")
        return self.book

        
if __name__=="__main__":
    centralLibrary= Library(["Algorithms","Django","Python","Clrs","Mathematics"])
    student= Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg ='''============Welcome to Central Library==============
        Please choose an option:
        1. List all the books
        2. Request a book
        3. return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a=int(input("Enter a choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBooks(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using this library")
            exit()
        else:
            print("Invalid input::")

        