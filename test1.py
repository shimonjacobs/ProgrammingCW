
books={} #dictionary containing books (format: {ISBN:[ISBN, title,author, Quantity]})

borrowedBooks={} #dictionary containing borrowed books (format: {ISBN:[ISBN, title,author, Quantity]})

def addBook(book):
    #add book to dictionary
    #book is a list containing [ISBN,title,author,year]
    books[book[0]] = book[1:]
    print("Book added successfully")

def removeBook():
    #remove book from dictionary
    ISBN = input("Enter ISBN of book to remove: ")
    if ISBN in books:
        del books[ISBN]
        print("Book removed successfully")
    else:
        print("Book not found")

def searchBook():
    #search for book by title
    title = input("Enter title of book to search for: ")
    found = False
    for book in books:
        if books[book][0] == title:
            print("Book found")
            print("ISBN: " + book)
            print("Title: " + books[book][0])
            print("Author: " + books[book][1])
            print("Year: " + books[book][2])
            found = True
    if not found:
        print("Book not found")

def listBooks():
    #list all books
    for book in books:
        print("ISBN: " + book)
        print("Title: " + books[book][0])
        print("Author: " + books[book][1])
        print("Year: " + books[book][2])
        print("")

def borrowBook():
    #borrow book
    ISBN = input("Enter ISBN of book to borrow: ")
    if ISBN in books:
        print("Book found")
        print("ISBN: " + ISBN)
        print("Title: " + books[ISBN][0])
        print("Author: " + books[ISBN][1])
        print("Year: " + books[ISBN][2])
        print("")
        print("Book borrowed successfully")
    else:
        print("Book not found")

def returnBook():
    #return book
    ISBN = input("Enter ISBN of book to return: ")
    if ISBN in books:
        print("Book found")
        print("ISBN: " + ISBN)
        print("Title: " + books[ISBN][0])
        print("Author: " + books[ISBN][1])
        print("Year: " + books[ISBN][2])
        print("")
        print("Book returned successfully")
    else:
        print("Book not found")



def LMS():
    print("Welcome to the Library Management System")
    print("Please select an option:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book by title")
    print("4. list all books")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            addBook()
        elif choice == "2":
            removeBook()
        elif choice == "3":
            searchBook()
        elif choice == "4":
            listBooks()
        elif choice == "5":
            borrowBook()
        elif choice == "6":
            returnBook()
        elif choice == "7":
            print("Thank you for using the Library Management System")
            break
        else:
            print("Invalid choice, please try again")

LMS()


    