from library import Library

library = Library()
is_library = True
while is_library:
    print("=== LIBRARY MANAGEMENT SYSTEM ===")
    print("1. View All Books\n2. Borrow a Book\n3. Return a Book\n4. Add a New Book\n5. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        library.display_all_books()
    elif user_input == "2":
        borrowed_id = input("Enter Book ID: ").lower().strip()
        library.borrow_book_by_id(borrowed_id)
    elif user_input == "3":
        return_id = input("Enter Return ID: ").lower().strip()
        library.return_book_by_id(return_id)
    elif user_input == "4":
        id_book = input("Enter Book ID: ").lower().strip()
        title = input("Enter Title: ").lower().strip()
        author = input("Enter Author: ").lower().strip()
        library.add_book(id_book, title, author)
    else:
        is_library = False