1
from library_functions import *

def main():
    catalogue = []
    users = []

    while True:
        print("\nLibrary System Menu")
        print("1. Load book catalogue from CSV")
        print("2. Save book catalogue to CSV")
        print("3. Add book")
        print("4. Display all books")
        print("5. Search by title")
        print("6. Search by author")
        print("7. Sort by title")
        print("8. Sort by year")
        print("9. Load users from CSV")
        print("10. Save users to CSV")
        print("11. Register library user")
        print("12. Display library user details")
        print("13. Pay fine")
        print("14. Borrow book")
        print("15. Return book")
        print("16. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter book CSV filename: ")
            catalogue = load_catalogue(filename)
        elif choice == '2':
            filename = input("Enter filename to save catalogue: ")
            save_catalogue(filename, catalogue)
        elif choice == '3':
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            isbn = input("ISBN: ")
            copies = int(input("Copies: "))
            add_book(catalogue, title, author, year, isbn, copies)
        elif choice == '4':
            display_books(catalogue)
        elif choice == '5':
            keyword = input("Enter title keyword: ")
            result = search_by_title(catalogue, keyword)
            display_books(result)
        elif choice == '6':
            author = input("Enter author name: ")
            result = search_by_author(catalogue, author)
            display_books(result)
        elif choice == '7':
            sort_by_title(catalogue)
            display_books(catalogue)
        elif choice == '8':
            sort_by_year(catalogue)
            display_books(catalogue)
        elif choice == '9':
            filename = input("Enter user CSV filename: ")
            users = load_users(filename)
        elif choice == '10':
            filename = input("Enter filename to save users: ")
            save_users(filename, users)
        elif choice == '11':
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            user_id = register_user(users, name, email, address)
        elif choice == '12':
            user_id = input("Library ID: ")
            display_user_details(users, user_id)
        elif choice == '13':
            user_id = input("Library ID: ")
            pay_fine(users, user_id)
            display_user_details(users, user_id)
        elif choice == '14':
            user_id = input("Library ID: ")
            book_title = input("Book title: ")
            borrow_book(users, catalogue, user_id, book_title)
        elif choice == '15':
            user_id = input("Library ID: ")
            book_title = input("Book title: ")
            return_date = input("Return date (YYYY-MM-DD): ")
            return_book(users, catalogue, user_id, book_title, return_date)
        elif choice == '16':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
