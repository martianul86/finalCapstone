class Book:
    def __init__(self, number, qty, title, author):
        self.id = number
        self.qty = qty
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book [id: {self.id}\tqty: {self.qty}\ttitle: {self.title}\tauthor: {self.author}]"


class BookStore:
    # Create empty list to hold books
    def __init__(self):
        self.bookList = []
     # Create new book and add it to the list
    def addNewBook(self, id, qty, title, author):
        self.bookList.append(Book(id, qty, title, author))
    # Remove book from the list
    def removeBook(self, id):
        b = self.searchBook(id)
        if b is not None:
            self.bookList.remove(b)

    def searchBook(self, id):
        for b in self.bookList:
            if b.id == id:
                return b

        return None
    # Function to update book
    def updateCurrentBook(self, id, title, author):
        if not self.bookList:
            return
        b = self.searchBook(id)
        b.title = title
        b.author = author
    # Creating the menu
    def showMenu():
        print("1. Enter book.")
        print("2. Update book.")
        print("3. Delete book.")
        print("4. Search books.")
        print("5. Exit.")
        print("Enter choice: ", end="")

    def run(self):
        print("Welcome to book Store:")
        number, qty, title, author = 0, 0, "", ""
        choice = 0
        while choice != 5:
            BookStore.showMenu()
            choice = int(input())
             # Get book details from user and add it to the list
            if choice == 1:
                number = int(input("Enter book id: "))
                qty = int(input("Enter book quantity: "))
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                self.addNewBook(number, qty, title, author)
            elif choice == 2:
                 # Get book id from user, search for the book and update its details
                number = int(input("Enter book id: "))
                b = self.searchBook(number)
                if b is None:
                    print("No such book.")
                else:
                    title = input("Enter new book title: ")
                    author = input("Enter new book author: ")
                    self.updateCurrentBook(number, title, author)
            elif choice == 3:
                # Get book id from user and remove it from the list
                number = int(input("Enter book id: "))
                self.removeBook(number)
            elif choice == 4:
                 # get book id from user and display book details
                number = int(input("Enter book id: "))
                b = self.searchBook(number)
                if b is None:
                    print("No such book.")
                else:
                    print(b)

        print("Goodbye!")


if __name__ == "__main__":
    store = BookStore()
    store.run()
