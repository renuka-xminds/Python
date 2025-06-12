class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies

    def checkAvailability(self):
        print(f"Total available copies: {self.available_copies}")
        return self.available_copies > 0

    def borrowBook(self, numberofbooks, *names):
        if self.checkAvailability():
            if self.available_copies >= numberofbooks:
                self.available_copies -= numberofbooks
                print(f"After borrowing, available copies: {self.available_copies}")
                print(f"Borrowed books are: {names}")
                return True
            else:
                print("Not enough copies available.")
        else:
            print("Book not available.")
        return False

    def returnBook(self, numberofbooks):
        self.available_copies += numberofbooks
        print(f"After return, available copies: {self.available_copies}")
        return self.available_copies


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, number, *names):
        if book.borrowBook(number, *names):
            self.borrowed_books.append((book.title, number, names))

    def return_book(self, book, number):
        book.returnBook(number)

    def display_borrowed_books(self):
        return self.borrowed_books


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn, total_copies, available_copies):
        book = Book(title, author, isbn, total_copies, available_copies)
        self.books.append(book)
        return book

    def add_member(self, member_id, name):
        member = Member(member_id, name)
        self.members.append(member)
        return member

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    
library = Library()

# Add book and member
book1 = library.add_book("Odail innum", "P Keshava Dev", "b123", 100, 50)
member1 = library.add_member(1, "Renuka")

# Borrow and return
print(book1.checkAvailability())
member1.borrow_book(book1, 10, "test1", "test2")
member1.return_book(book1, 5)
print("Borrowed books:", member1.display_borrowed_books())

# Find book
found_book = library.find_book("Odail innum")
print("Found book:", found_book.title if found_book else "Not found")
