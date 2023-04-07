import sqlite3

FILE_NAME = "books.db"

MENU = """Reading List
1. Add book
2. View books
3. Search book
4. Update book
5. Remove book
6. Quit
Your choice: """


def connect_to_database():
    conn = sqlite3.connect('FILE_NAME')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (title text, author text, year text)''')
    conn.commit()
    return conn

def add_book(conn):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    print("Book added successfully.")

def print_books(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    if len(rows) > 0:
        for row in rows:
            print("Title: {}, Author: {}, Year: {}".format(row[0], row[1], row[2]))
    else:
        print("No books found.")

def search_book(conn):
    title = input("Enter the title of the book you want to search for: ")
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE lower(title) = lower(?)", (title,))
    rows = c.fetchall()
    if len(rows) > 0:
        for row in rows:
            print("Title: {}, Author: {}, Year: {}".format(row[0], row[1], row[2]))
    else:
        print("Book not found.")

def update_book(conn):
    title = input("Enter the title of the book you want to update: ")
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE lower(title) = lower(?)", (title,))
    rows = c.fetchall()
    if len(rows) == 0:
        print("Book not found.")
        return
    author = input("Enter the new author's name (leave blank to keep the existing one): ")
    year = input("Enter the new year of publication (leave blank to keep the existing one): ")
    if author == '':
        author = rows[0][1]
    if year == '':
        year = rows[0][2]
    c.execute("UPDATE books SET author = ?, year = ? WHERE lower(title) = lower(?)", (author, year, title))
    conn.commit()
    print("Book updated successfully.")

def remove_book(conn):
    title = input("Enter the title of the book you want to remove: ")
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE lower(title) = lower(?)", (title,))
    rows = c.fetchall()
    if len(rows) == 0:
        print("Book not found.")
        return
    c.execute("DELETE FROM books WHERE lower(title) = lower(?)", (title,))
    conn.commit()
    print("Book removed successfully.")


def main():
    while True:
        choice = int(input(MENU))
        if choice == 1:
            add_book()
        elif choice == 2:
            print_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            update_book()
        elif choice == 5:
            remove_book()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()