def add_book(catalog, book_id, title, author, year):
    """Add a new book to the catalog dictionary."""
    catalog[book_id] = (title, author, year)
    print(f"Added book: {title}")

def borrow_book(catalog, borrowed_books, book_id):
    """Borrow a book if it exists and is not already borrowed."""
    if book_id not in catalog:
        print(f"Error: Book ID {book_id} does not exist in the catalog.")
    elif book_id in borrowed_books:
        print(f"Sorry: Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        title = catalog[book_id][0]
        print(f"Successfully borrowed: {title}")

def return_book(borrowed_books, book_id):
    """Return a borrowed book."""
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Successfully returned book ID: {book_id}")
    else:
        print(f"Error: Book ID {book_id} was not borrowed.")

def register_member(members, member_id):
    """Register a new member silently ignoring duplicates."""
    if member_id in members:
        print(f"Member ID {member_id} is already registered.")
    else:
        members.add(member_id)
        print(f"Successfully registered member ID: {member_id}")

def show_available(catalog, borrowed_books):
    """Print all books that are NOT in borrowed_books."""
    print("\n--- Available Books ---")
    available_found = False
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id} | Title: '{title}' by {author} ({year})")
            available_found = True
    
    if not available_found:
        print("No books available right now.")
    print("-----------------------\n")

def main():
    # Initialize our data structures
    catalog = {}          # Dictionary to map book_id -> (title, author, year)
    borrowed_books = []   # List to track borrowed books in order
    members = set()       # Set to track unique member IDs

    # 1. Add 4 books
    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "1984", "George Orwell", 1949)
    add_book(catalog, 103, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 104, "Moby Dick", "Herman Melville", 1851)
    
    # 2. Register 3 members (try adding the same member twice)
    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M002") # Duplicate attempt

    # 3. Display available books initially
    show_available(catalog, borrowed_books)

    # 4. Borrow 2 books
    borrow_book(catalog, borrowed_books, 102)
    borrow_book(catalog, borrowed_books, 104)

    # 5. Try to borrow an already borrowed book
    borrow_book(catalog, borrowed_books, 102)

    # 6. Show available books after borrowing
    show_available(catalog, borrowed_books)

    # 7. Return 1 book
    return_book(borrowed_books, 104)

    # 8. Show available books finally
    show_available(catalog, borrowed_books)

if __name__ == "__main__":
    main()
