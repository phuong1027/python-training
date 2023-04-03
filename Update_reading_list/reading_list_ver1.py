import csv

FILE_NAME = "books.csv"

MENU = """Reading List
1. Add book
2. View books
3. Search book
4. Update book
5. Remove book
6. Quit
Your choice: """


def init():
    try:
        with open(FILE_NAME, mode='x') as f:
            f.write("Title,Author,Release Year,Price,Rating\n")
    except:
        pass


def input_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    price = input("Enter the price of the book: ")
    rating = input("Enter your rating for the book (out of 5): ")
    return title, author, year, price, rating


def add_book():
    title, author, year, price, rating = input_book()
    with open(FILE_NAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, author, year, price, rating])
    print("The book's added successfully.")


def print_books():
    with open(FILE_NAME, 'r') as csvfile:
        # next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            print("Title: {}, Author: {}, Year: {}, Price: {}, Rating: {}".format(row[0], row[1], row[2], row[3], row[4]))


def search_book():
    title = input("Enter the title of the book you want to search for: ")
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == title.lower():
                print("Title: {}, Author: {}, Year: {}, Price: {}, Rating: {}".format(row[0], row[1], row[2], row[3], row[4]))
                return
        print("Book not found.")


def update_book():
    title = input("Enter the title of the book you want to update: ")
    books = []
    found = False

    with open(FILE_NAME, 'r') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:

            data = row

            if row[0].lower() == title.lower():
                data = [*input_book()]
                found = True

            books.append(data)

    if not found:
        print(f"`{title}` not found.")
    else:
        with open(FILE_NAME, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Author", "Release Year", "Price", "Rating"])
            writer.writerows(books)


def remove_book():
    title = input("Enter the title of the book you want to remove: ")
    books = []

    with open(FILE_NAME, 'r') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() != title.lower():
                books.append(row)

    with open(FILE_NAME, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Author", "Release Year", "Price", "Rating"])
        writer.writerows(books)


def main():
    init()
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
