class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
        
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You have checked out '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is already checked out.")
                return
        print(f"No book with title '{title}' found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{book.title}' has been returned. Thank you!")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        print(f"No book with title '{title}' found.")

    def list_available_books(self):
        print("Available books:")
        found = False
        for book in self._books:
            if book.is_available():
                print(f"- {book.title} by {book.author}")
                found = True
        if not found:
            print("No books available right now.")