class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")

        else:
            print("Books in library:")

            for book in self.books:
                print("-", book)

    def search_book(self, book):
        if book in self.books:
            print("Book is available.")
        else:
            print("Book not found.")


library = Library()

while True:
    print("\n1. Add book")
    print("2. Display books")
    print("3. Search book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book = input("Enter book name: ")
        library.search_book(book)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")