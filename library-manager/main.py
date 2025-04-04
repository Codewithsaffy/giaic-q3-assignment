from pymongo import MongoClient


client = MongoClient("mongodb+srv://sultan12332:sultan12332@cluster0.0srnmcx.mongodb.net/")
library_manager = client["library_manager"]
book_collection = library_manager["book"]



def load_library():
    """Load all books from the collection."""
    return list(book_collection.find())

def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    
    try:
        publication_year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the year.")
        return

    genre = input("Enter genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False
    
    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read": read
    }
    
    result = book_collection.insert_one(book)
    print(f"Book '{title}' added successfully with id: {result.inserted_id}.")

def remove_book():
    """Remove a book from the library by selecting its number."""
    library = load_library()
    if not library:
        print("No books to remove.")
        return

    print("Select a book to remove:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book.get('title', 'No Title')} by {book.get('author', 'Unknown Author')}")
    
    try:
        index = int(input("Enter the number of the book to remove: "))
        if index < 1 or index > len(library):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    book_to_remove = library[index - 1]
    remove_id = book_to_remove["_id"]
    result = book_collection.delete_one({"_id": remove_id})
    
    if result.deleted_count:
        print(f"Book '{book_to_remove.get('title', 'Unknown Title')}' removed successfully.")
    else:
        print("Error: Book could not be removed.")

def search_book():
    """Search for a book by title or author."""
    library = load_library()
    if not library:
        print("Library is empty.")
        return

    search_by = input("Search by Title or Author? (title/author): ").strip().lower()
    if search_by not in ("title", "author"):
        print("Invalid search criteria. Please choose 'title' or 'author'.")
        return

    search_term = input("Enter search term: ").strip().lower()
    
    if search_by == "title":
        results = [book for book in library if search_term in book.get("title", "").lower()]
    else:
        results = [book for book in library if search_term in book.get("author", "").lower()]
    
    if results:
        print("\nMatching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book.get("read") else "Unread"
            print(f"{idx}. {book.get('title')} by {book.get('author')} ({book.get('publication_year')}) - {book.get('genre')} - {status}")
    else:
        print("No matching books found.")

def display_all_books():
    """Display all books in the library."""
    library = load_library()
    if library:
        print("\nYour Library:")
        for idx, book in enumerate(library, 1):
            status = "Read" if book.get("read") else "Unread"
            print(f"{idx}. {book.get('title')} by {book.get('author')} ({book.get('publication_year')}) - {book.get('genre')} - {status}")
    else:
        print("Your library is empty.")

def display_statistics():
    """Display statistics about the library."""
    library = load_library()
    total = len(library)
    read_count = sum(1 for book in library if book.get("read"))
    percentage = (read_count / total * 100) if total > 0 else 0
    print("\nLibrary Statistics:")
    print(f"Total Books: {total}")
    print(f"Percentage of Books Read: {percentage:.1f}%")

def main():
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


