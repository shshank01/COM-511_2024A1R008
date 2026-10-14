'''Write a Python program that allows a librarian to add several books to a library. 
For each book, ask the user to enter its title and the number of copies. 
Store each book and its available copy count in a dictionary.
After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.

Apply these conditions:

Book titles should be compared without distinguishing uppercase and lowercase letters.
A book can be issued only if it exists in the library and at least one copy is available
Issuing a book decreases its available copy count by one.
A book can be returned only if it exists in the library and at least one copy has already been issued.
Returning a book increases its available copy count by one.
Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of coples.'''

class Library:
    def __init__(self):
        self.books={}
        self.issued={}
    def add_books(self,title,copies):
        title=title.lower()
        if title in self.books:
            self.books[title]+=copies
        else:
            self.books[title]=copies
            self.issued[title]=0
    def issue_book(self,title):
        title=title.lower()
        if title in self.books and self.books[title]>0:
            self.books[title]-=1
            self.issued[title]+=1
            print(f"Book {title} issued successfully.")
        else:
            print(f"Book {title} is not available for issuing.")
    def return_book(self,title):  # return the book only if at least one copy has been issued
        title=title.lower()
        if title in self.books and self.issued[title]>0:
            self.books[title]+=1
            self.issued[title]-=1
            print(f"Book {title} returned successfully.")
        else:
            print(f"Book {title} does not exist in the library.")
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for title, copies in self.books.items():
                print(f" {title}: {copies} ")
lib=Library()
while True:
    print("\n Library Menu: ")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        n=int(input("Enter number of books to add: "))
        for _ in range(n):
            title=input("Enter book title: ")
            copies=int(input("Enter number of copies: "))
            if copies<0:
                print("Invalid number of copies.")
            else:
                lib.add_books(title,copies)
    elif choice==2:
        title=input("Enter book title to issue: ")
        lib.issue_book(title)
    elif choice==3:
        title=input("Enter book title to return: ")
        lib.return_book(title)
    elif choice==4:
        lib.display_books()
    elif choice==5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

