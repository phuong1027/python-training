"""
It reads the file, skips the first line, then reads the rest of the lines, splits them on the comma,
and then creates a dictionary from the header and the line
"""
from pymongo import MongoClient

BOOK_DB = "BookDB"
BOOK_COL = "book"
CONN_STRING = "mongodb://localhost:27017"


def connect_db():
    client = MongoClient(CONN_STRING)
    book_db = client["BookDB"]
    return book_db["book"] # collection in MongoDB


MENU = """Welcome to the program
1. Add new book
2. show list books
3. search books
4. update book
5. remove book
6. quit
Your choice: """


def enter_book_col():
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    price = float(input("Price: "))
    rating = float(input("Rating: "))

    return {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "rating": rating
    }


def add_book():
    """
    It takes user input and writes it to a file.
    """
    book_col = enter_book_col()
    db_col = connect_db()
    db_col.insert_one(book_col)
    


def show_book_details(id, book):
    print(f"{id}: {repr(book['title'])} - {repr(book['author'])} - {book['year']} - {book['price']} - {book['rating']}")


def get_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """
    books = []

    book_col = connect_db()

    for doc in book_col.find():
        book = {}

        for key, value in doc.items():
            if key != '_id':
                book[key] = value
        
        books.append(book)

    if books:
        for id, book in enumerate(books, start=1):
            show_book_details(id, book)
    else:
        print("The books is empty!")


def search_book():
    """
    It takes a book title as input, loads the JSON data from the return_all_book() function, and then
    loops through the data to find the book with the matching title.
    """
    """
    It takes a book title as input, loads the JSON data from the return_all_book() function, and then
    loops through the data to find the book with the matching title
    """
    search_title = input("Enter the book title: ")
    found = False

    book_col = connect_db()

    for id, doc in enumerate(book_col.find(), start=1):

        if doc['title'] == search_title:
            show_book_details(id, doc)
            found = True
                
    
    if not found:
        print(f"`{search_title}` is not found!")


def update_book():
    search_title = input("Enter the book title: ")
    found = False
    book_col = connect_db()

    for doc in book_col.find():

        if doc['title'] == search_title:
            found = True

    if found:
        myquery = { "title": search_title }
        newvalues = { "$set": enter_book_col()}
        book_col.update_one(myquery, newvalues)
    else:
        print(f'`{search_title}` is not found!')



def remove_book():
    search_title = input("Enter the book title: ")
    found = False
    book_col = connect_db()

    for doc in book_col.find():

        if doc['title'] == search_title:
            found = True

    if found:
        my_query = {'title': search_title}
        book_col.delete_one(my_query)
    else:
        print(f'`{search_title}` is not found!')


# The main function of the program. It is the first thing that runs when the program is executed.
choice = int(input(MENU))

operations = (add_book, get_all_book, search_book, update_book, remove_book)

while choice != 6:
    if choice in range(1, len(operations) + 1):
        operations[choice - 1]()
    else:
        print("Invalid choice. Please try again.")
    print()
    choice = int(input(MENU))

