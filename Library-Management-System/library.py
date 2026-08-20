from book import Book
class Library:
    def __init__(self):
        self.books = {}
        for book_title, info in self.books.items():
            self.books[book_title] = Book(book_title, info['title'], info['author'], info['is_borrowed'])

    def add_book(self, book_id, book_title, book_author, book_is_borrowed= False):
        if book_id in self.books:
            print(f"Book ID '{book_id}' already exists in the catalog!")
            return False
        else:
            self.books[book_id] = Book(book_id, book_title, book_author, book_is_borrowed)
            return True

    def display_all_books(self):
        if None in self.books:
            print("There are currently no books in the library.")
            print("----------------------------------------------")
        else:
            for book_id, book in self.books.items():
                print(f"Book ID: {book_id}, Title: {book.title}, Author: {book.author}")

    def borrow_book_by_id(self, book_id):
        if book_id in self.books:
            self.books[book_id].borrow_book()
            return True
        else:
            print(f"Book ID '{book_id}' does not exist in the catalog!")
            return False

    def return_book_by_id(self, book_id):
        if book_id in self.books:
            self.books[book_id].return_book(book_id)
            return True
        else:
            print(f"Book ID '{book_id}' does not exist in the catalog!")
            return False

# library = Library()
# library.add_book("B102", "One piece", "Echiro Oda")
# id_book = input("Enter Book ID: ")
# title = input("Enter Title: ")
# author = input("Enter Author: ")
# library.add_book(id_book, title, author)
# print(library.books)
# library.display_all_books()
# borrowed_id = input("Enter Book ID: ")
# library.borrow_book_by_id(borrowed_id)
# return_id = input("Enter Return ID: ")
# library.return_book_by_id(return_id)