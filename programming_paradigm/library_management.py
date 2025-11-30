class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_check_out = False

    def check_out(self):
        if not self._is_check_out:
            self._is_check_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_check_out:
            self._is_check_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_check_out
    

class Library:
    def __init__(self):
        self._books = []        # Let protect the list of store Books instatnces
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.check_out()
            return None
    
    def list_available_books(self):
        found_availabe = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                found_available = True

        if not found_available:
            print("No book currently avaialble")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return None
