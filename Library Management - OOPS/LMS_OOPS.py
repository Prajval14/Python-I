"""
Author : Prajval Patel (C0911611)
Date : November 14th, 2023
Program : Implementing a Library Management System without Inheritance
"""


# Part 1: Define Book-related Classes
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
            print(f'{self.title} is checked out successfully. Thank you.')
        else:
            print('The requested book is not available at the moment, please come back later.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'{self.title} returned successfully. Thank you.')
        else:
            print('Unable to return book. Try Again.')

    def __str__(self):
        if self.available:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Available'
        else:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Not Available'


class FictionBook:
    def __init__(self, title, author, isbn, genre, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = available

    def __str__(self):
        if self.available:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Available'
        else:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Not Available'


class NonFictionBook:
    def __init__(self, title, author, isbn, field, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.field = field
        self.available = available

    def __str__(self):
        if self.available:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Available'
        else:
            return f'{self.title} by {self.author} (ISBN: {self.isbn}) - Not Available'


#Part 2: Define the Library Class
class Library:
    def __init__(self):
        self.book_list = []
        self.fiction_book_list = []
        self.nonfiction_book_list = []

    def add_book(self, book, book_type):
        if book_type == 'Book':
            self.book_list.append(book)
        elif book_type == 'FictionBook':
            self.fiction_book_list.append(book)
        elif book_type == 'NonFictionBook':
            self.nonfiction_book_list.append(book)
        else:
            print('Invalid book type. Please provide valid category.')

    def list_books(self):
        print('All Books:')
        for book in self.book_list:
            print(book)
        print('\nFiction Books:')
        for book in self.fiction_book_list:
            print(book)
        print('\nNon-Fiction Books:')
        for book in self.nonfiction_book_list:
            print(book)

    def checkout_book(self, title, book_type):
        book_list = self.get_book_list_by_type(book_type)
        for book in book_list:
            if book.title == title and book.available:
                book.checkout()
                return
        print(f'{title} not available for checkout.')

    def return_book(self, title, book_type):
        book_list = self.get_book_list_by_type(book_type)
        for book in book_list:
            if book.title == title and not book.available:
                book.return_book()
                return
        print(f'{title} was not returned. Please check if the category is correct and try again.')

    def get_book_list_by_type(self, book_type):
        if book_type == 'Book':
            return self.book_list
        elif book_type == 'FictionBook':
            return self.fiction_book_list
        elif book_type == 'NonFictionBook':
            return self.nonfiction_book_list
        else:
            return []


#-------------Testing----------------

#Initializing library object for Library class
library = Library()

#Initializing data for different categories
book1 = Book('Test', 'Test', '1234567890')
fiction_book1 = FictionBook('Test1', 'Test1', '1234567890', 'Test1')
nonfiction_book1 = NonFictionBook('Test2', 'Test2', '1234567890', 'Test2')

#Adding data in different list by passing book object and category
library.add_book(book1, 'Book')
library.add_book(fiction_book1, 'FictionBook')
library.add_book(nonfiction_book1, 'NonFictionBook')

#Testing updated book list
library.list_books()

#Checking out a book by passing book name and category
library.checkout_book('Test', 'Book')

#Testing updated book list
library.list_books()

#Returning a book by passing book name and category
library.return_book('Test', 'Book')

#Testing updated book list
library.list_books()

#Testcase for wrong book
library.checkout_book('Test1', 'Book')

#Testcase for wrong category
library.checkout_book('Test', 'Book2')

#Testcase for wrong book
library.return_book('Test1', 'Book')

#Testcase for wrong category
library.return_book('Test', 'Book2')


