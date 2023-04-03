import csv

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    with open('books.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, author, year])
    print("Book added successfully.")

def print_books():
    with open('books.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("Title: {}, Author: {}, Year: {}".format(row[0], row[1], row[2]))

def search_book():
    title = input("Enter the title of the book you want to search for: ")
    with open('books.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == title.lower():
                print("Title: {}, Author: {}, Year: {}".format(row[0], row[1], row[2]))
                return
        print("Book not found.")

def main():
    while True:
        print("Reading List\n")
        print("1. Add book")
        print("2. View books")
        print("3. Search book")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            print_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()