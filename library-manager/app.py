import streamlit as st
import json
import os

# File where our library will be stored
LIBRARY_FILE = "library.json"

def load_library():
    """Loads the library from a file if it exists, otherwise returns an empty list."""
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                library = json.load(file)
            return library
        except json.JSONDecodeError:
            st.error("Oops, there was an error reading your library file. Starting fresh!")
            return []
    else:
        return []

def save_library(library):
    """Saves the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)
    st.success("Your library has been saved!")

# Use session state to persist the library during the app's run
if 'library' not in st.session_state:
    st.session_state.library = load_library()

def add_book():
    st.header("Add a New Book")
    with st.form("add_book_form", clear_on_submit=True):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        publication_year = st.text_input("Publication Year (use a number)")
        genre = st.text_input("Genre")
        read = st.radio("Have you read this book?", ["Yes", "No"])
        submit = st.form_submit_button("Add Book")

        if submit:
            try:
                year = int(publication_year)
            except ValueError:
                st.error("Please enter a valid number for the publication year.")
                return
            
            # Create a new book entry
            book = {
                "title": title,
                "author": author,
                "publication_year": year,
                "genre": genre,
                "read": True if read == "Yes" else False
            }
            st.session_state.library.append(book)
            st.success(f"Book '{title}' added successfully!")
            save_library(st.session_state.library)

def remove_book():
    st.header("Remove a Book")
    with st.form("remove_book_form", clear_on_submit=True):
        title = st.text_input("Enter the title of the book you want to remove")
        submit = st.form_submit_button("Remove Book")
        if submit:
            removed = False
            for book in st.session_state.library:
                if book["title"].lower() == title.lower():
                    st.session_state.library.remove(book)
                    removed = True
                    st.success(f"Book '{title}' removed successfully!")
                    save_library(st.session_state.library)
                    break
            if not removed:
                st.warning("Hmm, we couldn't find that book in your library.")

def search_book():
    st.header("Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    search_term = st.text_input(f"Enter the {search_by.lower()} to search for:")
    
    if st.button("Search"):
        if search_term:
            if search_by == "Title":
                results = [book for book in st.session_state.library if search_term.lower() in book["title"].lower()]
            else:
                results = [book for book in st.session_state.library if search_term.lower() in book["author"].lower()]
            if results:
                st.subheader("Matching Books:")
                for idx, book in enumerate(results, 1):
                    status = "Read" if book["read"] else "Unread"
                    st.write(f"{idx}. **{book['title']}** by *{book['author']}* ({book['publication_year']}) - {book['genre']} - {status}")
            else:
                st.info("No matching books found. Try a different search term!")
        else:
            st.warning("Please enter something to search for.")

def display_all_books():
    st.header("Your Library")
    if st.session_state.library:
        for idx, book in enumerate(st.session_state.library, 1):
            status = "Read" if book["read"] else "Unread"
            st.write(f"{idx}. **{book['title']}** by *{book['author']}* ({book['publication_year']}) - {book['genre']} - {status}")
    else:
        st.info("Your library is empty. Start adding some books!")

def display_statistics():
    st.header("Library Statistics")
    total = len(st.session_state.library)
    read_count = sum(1 for book in st.session_state.library if book["read"])
    percentage = (read_count / total * 100) if total > 0 else 0
    st.write(f"**Total Books:** {total}")
    st.write(f"**Percentage of Books Read:** {percentage:.1f}%")

# Main app interface
st.title("Personal Library Manager")
st.write("Welcome to your Personal Library Manager! Use the sidebar to navigate through the options.")

menu = st.sidebar.radio("Menu", 
                        ("Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"))

if menu == "Add a Book":
    add_book()
elif menu == "Remove a Book":
    remove_book()
elif menu == "Search for a Book":
    search_book()
elif menu == "Display All Books":
    display_all_books()
elif menu == "Display Statistics":
    display_statistics()
