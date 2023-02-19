#==== LIBRARIES

import sqlite3
import os.path


#==== FUNCTIONS ====

## Check if a database file exists
def check_file_exists():

    path = './ebookstore.db'
    check_file = os.path.exists(path)

    if check_file == True:
        menu()
    else:
        create_table()
        populate_initial()
        menu()


## Main menu
def menu():

    menu = input("""\nPlease select one of the following options:
1\t- Enter book
2\t- Update book
3\t- Delete book
4\t- Search book
0\t- Exit
: """)

    if menu == "1":
        enter_book()

    elif menu == "2":
        update_book()

    elif menu == "3":
        delete_book()

    elif menu == "4":
        search_book()

    elif menu == "0":
        print("\nGoodbye!")
        exit()

    else:
        print("\nYou have made a wrong choice. Please try again.")


## Create table
def create_table():    

    # Connect to database
    conn = sqlite3.connect('ebookstore.db')

    # Create a cursor
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Qty INTEGER
    )""")

    print("Table created successfully.")

    # Commit command
    conn.commit()

    # Close the connection
    conn.close()


## Populate table with initial book list
def populate_initial():    
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()

    # Initial book list
    initial_books = [
                    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
                    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
                    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
                    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
                    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
                    ]
    
    # Add initial books to table
    try:
        c.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", initial_books)
    except Exception as e:
        conn.rollback()

    print("Records added successfully")

    conn.commit()
    conn.close()


## View current table
def view_table():    
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()

    # View current table
    c.execute("SELECT * FROM books")
    books = c.fetchall()

    for book in books:
        print(f"{book[0]} | {book[1]} by {book[2]} | Qty: {book[3]}")

    conn.commit()
    conn.close()


## Enter book
def enter_book():
    # User inputs for book details
    title = input("\nEnter the title of the book: ")
    author = input("Enter the name of the author: ")
    
    # Try/Except for integer
    while True:
        try:
            quantity = int(input("Enter the quantity of books:  "))
        except ValueError:
            print("\nSorry. That is not a valid input.")
            continue
        else:
            break

    # Confirm inputs
    confirm = input(f"""\nYou have entered the following:
Title:\t\t{title}
Author:\t\t{author}
Quantity:\t{quantity}

Is this correct? (Yes/No): """).lower()

    while confirm not in ["yes", "no"]:
        print("Sorry. That is not a valid input.")
        confirm = input(f"""\nYou have entered the following:
Title:\t\t{title}
Author:\t\t{author}
Quantity:\t{quantity}

Is this correct? (Yes/No): """).lower()

    # Enter book details into database
    if confirm == "yes":
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        c.execute("""
            INSERT INTO books(Title, Author, Qty)
            VALUES (?, ?, ?)
            """, (title, author, quantity))
        conn.commit()
        conn.close()
        print("\nField added successfully.")
    else:
        print("\nOperation aborted. Return to main menu.")


## Update book
def update_book():
    print("\nHere is the current stock:\n")
    view_table()

    # Check if the book exists in the database
    while True:
        try:
            select_id = int(input("\nEnter the ID of the stock you would like to update: "))

            conn = sqlite3.connect('ebookstore.db')
            c = conn.cursor()
            c.execute("""SELECT id
            FROM books
            WHERE id = ?""", (select_id,))
            result = c.fetchone()

            if result is None:
                print("""\nNo such record exists.
Operation aborted. Return to main menu.""")
                conn.close()
            else:
                # Enter new stock quantity
                while True:
                    try:
                        new_stock = int(input("\nEnter the quantity of the updated stock: "))

                        # Confirm inputs
                        confirm = input(f"\nUpdate quantity of book ID {select_id} to {new_stock}? (Yes/No): ").lower()

                        while confirm not in ["yes", "no"]:
                            print("Sorry. That is not a valid input.")
                            confirm = input(f"\nUpdate quantity of books with ID {select_id} to {new_stock}? (Yes/No): ").lower()

                        # Update book details in database
                        if confirm == "yes":
                            conn = sqlite3.connect('ebookstore.db')
                            c = conn.cursor()

                            c.execute("""
                                UPDATE books
                                SET Qty = ?
                                WHERE id = ?
                                """, (new_stock, select_id))
                            conn.commit()
                            conn.close()
                            print("\nField updated successfully.")
                        else:
                            print("\nOperation aborted. Return to main menu.")
                    
                    except ValueError:
                        print("\nSorry. That is not a valid input.")
                        continue
                    else:
                        break                    
        
        except ValueError:
            print("\nSorry. That is not a valid input.")
            continue
        else:
            break


## Delete book
def delete_book():
    print("\nHere is the current stock:\n")
    view_table()

    # Check if the book exists in the database
    while True:
        try:
            select_id = int(input("\nEnter the ID of the books you would like to delete: "))

            conn = sqlite3.connect('ebookstore.db')
            c = conn.cursor()
            c.execute("""SELECT id
            FROM books
            WHERE id = ?""", (select_id,))
            result = c.fetchone()

            if result is None:
                print("""\nNo such record exists.
Operation aborted. Return to main menu.""")
                conn.close()
            else:
                # Confirm inputs
                confirm = input(f"\nDelete books with ID {select_id}? (Yes/No): ").lower()

                while confirm not in ["yes", "no"]:
                    print("Sorry. That is not a valid input.")
                    confirm = input(f"\nDelete books with ID {select_id}? (Yes/No): ").lower()

                # Delete books from database
                if confirm == "yes":
                    conn = sqlite3.connect('ebookstore.db')
                    c = conn.cursor()

                    c.execute("""
                        DELETE FROM books
                        WHERE id = ?
                        """, (select_id,))
                    conn.commit()
                    conn.close()
                    print("\nField deleted successfully.")
                else:
                    print("\nOperation aborted. Return to main menu.")

        except ValueError:
            print("\nSorry. That is not a valid input.")
            continue
        else:
            break


## Search book
def search_book():
    
    search_menu = input("""\nHow would you like to search?
1\t- by Title
2\t- by Author
: """)

    # Search by title
    if search_menu == "1":
        search_title = input("\nEnter the title of the book: ")
        search_title = ('%' + search_title + '%')

        # Check database for partial string matches
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("""
            SELECT *
            FROM books
            WHERE Title LIKE ?""", (search_title,))
        result = c.fetchone()

        if result is None:
            print("""\nNo such record exists.
Operation aborted. Return to main menu.""")
            conn.close()
        else:
            c.execute("""
                SELECT *
                FROM books
                WHERE Title Like ?""", (search_title,))
            print("\nThe following item(s) are in stock:")
            for row in c:
                print(f"id: {row[0]} | {row[1]} by {row[2]} | Qty: {row[3]}")

    # Search by author
    elif search_menu == "2":
        search_author = input("\nEnter the author of the book: ")
        search_author = ('%' + search_author + '%')

        # Check database for partial string matches
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("""
            SELECT *
            FROM books
            WHERE Author LIKE ?""", (search_author,))
        result = c.fetchone()

        if result is None:
            print("""\nNo such record exists.
Operation aborted. Return to main menu.""")
            conn.close()
        else:
            c.execute("""
                SELECT *
                FROM books
                WHERE Author Like ?""", (search_author,))
            print("\nThe following item(s) are in stock:")
            for row in c:
                print(f"id: {row[0]} | {row[1]} by {row[2]} | Qty: {row[3]}")

    else:
        print("\nSorry. That is not a valid input.")


#==== PROGRAM START ====

while True:

    check_file_exists()