class Book:
    total_books = 0
    def __init__(self, title):
        self.title = title
        Book.increase_total_books()

    @classmethod
    def increase_total_books(self):
        Book.total_books += 1
        print(f"Total books: {Book.total_books}")


book1 = Book("Book 1")
book2 = Book("Book 2")
book3 = Book("Book 3")

book4 = Book("Book 4")
book5 = Book("Book 5")
print(f"Total books: {Book.total_books}")