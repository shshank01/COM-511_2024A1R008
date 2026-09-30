'''
Write a Python Program to manage a small library using a dictionary.
The program must repeatedly allow the user to add books, issue books,return books, and display the current book record.

Conditions:
    1. Store book title as key and available copies as the value
    2. A book can be issued only if it exists and at least 1 copy is available.
    3. Return a book only if it already exists in the library record.
    4. Book names should work regardless of uppercase or lowercase letters.
'''
books={
    "book1":5,
    "book2":10,
    "book3":15  
}
while True:
    print("1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Display book record")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        book=input("Enter book name: ")
        copies=int(input("Enter number of copies: "))
        books[book]=copies
        print("Book added successfully")
    elif choice==2:
        book=input("Enter book name: ")
        if book in books:
            if books[book]>0:
                books[book]-=1
                print("Book issued successfully")
            else:
                print("Book not available")
        else:
            print("Book not found")
    elif choice==3:
        book=input("Enter book name: ")
        if book in books:
            books[book]+=1
            print("Book returned successfully")
        else:
            print("Book not found")
    elif choice==4:
        for book,copies in books.items():
            print(f"{book}: {copies}")
    elif choice==5:
        break
    else:
        print("Invalid choice")