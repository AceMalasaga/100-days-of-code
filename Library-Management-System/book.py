class Book:

    def __init__(self, book_id, title, author, is_borrowed):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display_info(self):
        if not self.is_borrowed:
            status = "Available"
        else:
            status = "Borrowed"
        if not self.book_id:
            print("There are currently no books in the library.")
        else:
            print("=== ALL BOOKS ===")
            print(f"[{self.book_id}] {self.title} by {self.author} - [{status}]")
            print("--------------------------------------------------------------")

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
            return True
        else:
            print(f"{self.title} is already borrowed.")
            return False

    def return_book(self, book_id):
        if self.is_borrowed:
            print(f"'{self.title}' has been returned to the library.")
            self.is_borrowed = False
            return True
        else:
            print(f"'{book_id}' was not borrowed.")
            return False

# book1 = Book("B102", "Pride and Prejudice", "Jane Austen", False)
# book = Book("B101", "To Kill a Mockingbird", "Harper Lee", True)
# book.display_info()
# book.borrow_book()
# book.return_book("B101")