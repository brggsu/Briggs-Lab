from typing import List, Optional
import csv
from datetime import datetime, timedelta

# Student Name: Joshnell Briggs Zareno
# Student Number: 12292861

# ---------------------------
# Phase 1: Book Catalogue
# ---------------------------

def load_catalogue(filename: str) -> List[dict]:
    """
    Load a book catalogue from a CSV file.

    Args:
        filename (str): The CSV file containing book records
                        (Title, Author, Year, ISBN, Copies).

    Returns:
        List[dict]: A list of book dictionaries.

    Raises:
        FileNotFoundError: If the file does not exist.
        KeyError: If the file format is invalid.
        ValueError: If Year or Copies cannot be converted to integers.
    """
    catalogue = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                catalogue.append({
                    "Title": row["Title"],
                    "Author": row["Author"],
                    "Year": int(row["Year"]),
                    "ISBN": row["ISBN"],
                    "Copies": int(row["Copies"])
                })
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except KeyError:
        print(f"Error: {filename} is not a valid book catalogue file.")
    except ValueError:
        print(f"Error: Invalid data format in {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(f"Catalogue loaded successfully from {filename}.")
    return catalogue

def save_catalogue(filename: str, catalogue: List[dict]) -> None:
    """
    Save a book catalogue to a CSV file.

    Args:
        filename (str): The CSV file to save the catalogue to.
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).

    Returns:
        None

    Raises:
        OSError: If the file cannot be created or written to.
    """
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["Title", "Author", "Year", "ISBN", "Copies"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for book in catalogue:
                writer.writerow({
                    "Title": book["Title"],
                    "Author": book["Author"],
                    "Year": book["Year"],
                    "ISBN": book["ISBN"],
                    "Copies": book["Copies"]
                })
    except OSError: 
        print(f"Error: Could not save to {filename}.")
    else:
        print(f"Catalogue saved successfully to {filename}.")

def add_book(catalogue: List[dict], title: str, author: str, year: int, isbn: str, copies: int) -> None:
    """
    Add a new book record to the catalogue.

    Args:
        catalogue (List[dict]): The list of existing book dictionaries.
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
        isbn (str): The ISBN identifier of the book.
        copies (int): The number of copies available.

    Returns:
        None

    Raises:
        None
    """
    book = {
        "Title": title,
        "Author": author,
        "Year": int(year),
        "ISBN": isbn,
        "Copies": int(copies)
    }
    catalogue.append(book)
    print("Book added successfully to catalogue!")

def display_books(booklist: List[dict]) -> None:
    """
    Display a list of books in a formatted table.

    Args:
        booklist (List[dict]): A list of book dictionaries containing
                               (Title, Author, Year, ISBN, Copies).

    Returns:
        None

    Raises:
        None
    """
    if not booklist:
        print("No books to display.")
        return

    print(f"{'Title':^40} {'Author':^20} {'Year':^10} {'ISBN':^20} {'Copies':^10}")
    print("-" * 105)
    for book in booklist:
        print(f"{book['Title'][:40]:^40} "
            f"{book['Author'][:20]:^20} "
            f"{book['Year']:^10} "
            f"{book['ISBN'][:20]:^20} "
            f"{book['Copies']:^10}")

def search_by_title(catalogue: List[dict], keyword: str) -> List[dict]:
    """
    Search for books in the catalogue by a keyword in the title.

    Args:
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).
        keyword (str): The search keyword to match against book titles
                       (case-insensitive).

    Returns:
        List[dict]: A list of book dictionaries whose titles contain
                    the given keyword.

    Raises:
        None
    """
    results = []
    if not keyword.strip():
        print("Error: Search keyword cannot be empty or spaces only.")
        return results
    for book in catalogue:
        if keyword.lower() in book["Title"].lower():
            results.append(book)
    return results 

def search_by_author(catalogue: List[dict], author: str) -> List[dict]:
    """
    Search for books in the catalogue by a keyword in the author's name.

    Args:
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).
        author (str): The search keyword to match against author names
                      (case-insensitive).

    Returns:
        List[dict]: A list of book dictionaries whose authors contain
                    the given keyword.

    Raises:
        None
    """
    results = []
    for book in catalogue:
        if not author.strip():
            print("Error: Search keyword cannot be empty or spaces only.")
            return results
        if author.lower() in book["Author"].lower():
            results.append(book)
    return results

def sort_by_title(catalogue: List[dict]) -> None:
    """
    Sort the book catalogue alphabetically by title.

    Args:
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).

    Returns:
        None

    Raises:
        None
    """
    catalogue.sort(key=lambda book: str(book.get("Title", "")).lower())
    print("Catalogue sorted by title successfully.")

def sort_by_year(catalogue: List[dict]) -> None:
    """
    Sort the book catalogue alphabetically by title.

    Args:
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).

    Returns:
        None

    Raises:
        None
    """
    catalogue.sort(key=lambda book: int(book.get("Year", 0)))
    print("Catalogue sorted by year successfully.")

# ---------------------------
# Phase 2: Library Users
# ---------------------------

def load_users(filename: str) -> List[dict]:
    """
    Load user records from a CSV file.

    Args:
        filename (str): The CSV file containing user records with fields
                        (ID, Name, Email, Address, Fine, BooksBorrowed).

    Returns:
        List[dict]: A list of user dictionaries, where each user contains:
            - ID (str): Unique user identifier.
            - Name (str): Full name of the user.
            - Email (str): Email address of the user.
            - Address (str): Postal address of the user.
            - Fine (float): Outstanding fine amount.
            - BooksBorrowed (List[dict]): A list of borrowed book records with:
                * Book Title (str)
                * Due Date (str)

    Raises:
        FileNotFoundError: If the specified file does not exist.
        KeyError: If required fields are missing in the CSV file.
        ValueError: If 'Fine' cannot be converted to float or data is invalid.
    """
    users = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Parse BooksBorrowed column
                books_raw = row.get("BooksBorrowed", "").strip()
                books_borrowed = []

                if books_raw:  # "1984|2025-07-15" to "{'Book Title': '1984', 'Due Date': '2025-07-15'}"
                    for entry in books_raw.split(";"): 
                        entry = entry.strip()
                        if "|" in entry:
                            title, due_date = entry.split("|", 1)
                            books_borrowed.append({
                                "Book Title": title.strip(),
                                "Due Date": due_date.strip()
                            })
                users.append({
                    "ID": row["ID"],
                    "Name": row["Name"],
                    "Email": row["Email"],
                    "Address": row["Address"],
                    "Fine": float(row.get("Fine", 0.00)),
                    "BooksBorrowed": books_borrowed,
                })
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except KeyError:
        print(f"Error: {filename} is not a valid user file.")
    except ValueError:
        print(f"Error: Invalid data format in {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(f"Users loaded successfully from {filename}.")
    return users

def save_users(filename: str, users: List[dict]) -> None:
    """
    Save user records to a CSV file.

    Args:
        filename (str): The CSV file to save the user records to.
        users (List[dict]): A list of user dictionaries containing:
            - ID (str): Unique user identifier.
            - Name (str): Full name of the user.
            - Email (str): Email address of the user.
            - Address (str): Postal address of the user.
            - Fine (float): Outstanding fine amount (formatted to 2 decimals).
            - BooksBorrowed (list): Borrowed book records.

    Returns:
        None

    Raises:
        OSError: If the file cannot be created or written to.
    """
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["ID", "Name", "Email", "Address", "Fine", "BooksBorrowed"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for user in users:
                writer.writerow({
                    "ID": user["ID"],
                    "Name": user["Name"],
                    "Email": user["Email"],
                    "Address": user["Address"],
                    "Fine": f"{float(user['Fine']):.2f}",
                    "BooksBorrowed": user["BooksBorrowed"]
                })
    except OSError: 
        print(f"Error: Could not save to {filename}.")
    else:
        print(f"Users saved successfully to {filename}.")

def register_user(users: List[dict], name: str, email: str, address: str) -> str:
    """
    Register a new user and assign a unique library ID.

    Args:
        users (List[dict]): The list of existing user dictionaries.
        name (str): Full name of the new user.
        email (str): Email address of the new user.
        address (str): Postal address of the new user.

    Returns:
        str: The newly assigned user ID in the format "LIBXXXX"
             (e.g., LIB0001, LIB0002).

    Raises:
        OSError: If the file cannot be created or written to.
    """
    if not users:
        next_id_num = 1
    else:
        existing_ids = [int(u["ID"].replace("LIB", "")) for u in users if u["ID"].startswith("LIB")]
        if existing_ids: # Checker if not empty
            next_id_num = max(existing_ids) + 1
        else:
            next_id_num = 1

    user_id = f"LIB{next_id_num:04d}"
    new_user = {
        "ID": user_id,
        "Name": name.strip(),
        "Email": email.strip(),
        "Address": address.strip(),
        "Fine": 0.0,
        "BooksBorrowed": []
    }

    users.append(new_user)
    print(f"User registered successfully with ID: {user_id}")
    return user_id

def display_user_details(users: List[dict], user_id: str) -> None:
    """
    Display the details of a specific user, including borrowed books.

    Args:
        users (List[dict]): A list of user dictionaries containing
                            (ID, Name, Email, Address, Fine, BooksBorrowed).
        user_id (str): The ID of the user to display (case-insensitive).

    Returns:
        None

    Raise:
        None

    Notes:
        - Prints an error message if no user is found with the given ID.
        - Displays borrowed books in a table format if available.
    """
    # Look for the user
    user = next((u for u in users if u["ID"] == user_id.upper()), None)

    if not user:
        print(f"Error: No user found with ID {user_id}.")
        return

    # Print basic details
    print("\n=== User Details ===")
    print(f"ID: {user['ID']}")
    print(f"Name: {user['Name']}")
    print(f"Email: {user['Email']}")
    print(f"Address: {user['Address']}")
    print(f"Outstanding Fine: ${float(user['Fine']):.2f}")

    # Print borrowed books in table format
    if not user["BooksBorrowed"]:
        print("Books Borrowed: None")
    else:
        print("\nBooks Borrowed:")
        print(f"{'Title':^40} {'Due Date':^15}")
        print("-" * 55)

        for book in user["BooksBorrowed"]:
            if isinstance(book, dict):
                title = book.get("Book Title", "")[:40]
                due   = book.get("Due Date", "")
                print(f"{title:^40} {due:^15}")
            else:
                # if BooksBorrowed is still a raw string
                print(f"{str(book):^55}")

def pay_fine(users: List[dict], user_id: str) -> None: 
    """
    Clear the outstanding fine for a specific user.

    Args:
        users (List[dict]): A list of user dictionaries containing
                            (ID, Name, Email, Address, Fine, BooksBorrowed).
        user_id (str): The ID of the user who's fine is to be cleared.

    Returns:
        None

    Raise:
        None

    Notes:
        - Resets the user's fine amount to 0.0 and confirms the update.
    """
    # Find the user
    user = next((u for u in users if u["ID"].lower() == user_id.lower()), None)

    if not user:
        return

    # Reset fine
    user["Fine"] = 0.0
    print(f"Fine for user {user['ID']} ({user['Name']}) has been cleared to $0.00.")

# ---------------------------
# Phase 3: Borrowing and Returning Books 
# ---------------------------

def borrow_book(users: List[dict], catalogue: List[dict], user_id: str, book_title: str) -> None:
    """
    Borrow a book for a user by searching titles with a keyword and update records.

    Args:
        users (List[dict]): A list of user dictionaries containing
                            (ID, Name, Email, Address, Fine, BooksBorrowed).
        catalogue (List[dict]): A list of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).
        user_id (str): The ID of the user borrowing the book (case-insensitive).
        book_title (str): A non-sensitive keyword to match against book titles
                          (case-insensitive).

    Returns:
        None

    Notes:
        - Prints error messages for: unknown user, outstanding fines, empty keyword,
          no matches, no available copies, or duplicate borrow.
        - If multiple matches are found, displays a table and prompts the user to
          select a book via input().
        - On success, appends {"Book Title": <title>, "Due Date": <YYYY-MM-DD>}
          to the user's BooksBorrowed list and decrements the book's Copies by 1.
    """
    # 1. Find user
    user = next((u for u in users if u.get("ID") == user_id.upper()), None)
    if not user:
        print(f"Error: No user found with ID {user_id.upper()}.")
        return

    # 2. Fine check
    fine = float(user.get("Fine", 0.0))
    if fine > 0.0:
        print(f"Error: User {user_id.upper()} has outstanding fines (${fine:.2f}). Please pay before borrowing.")
        return

    # 3. Keyword search (case-insensitive)
    search_term = book_title.strip().lower()
    if not search_term:
        print("Error: Search keyword cannot be empty.")
        return

    matches = [b for b in catalogue if search_term in str(b.get("Title", "")).lower()]
    if not matches:
        print(f"No books found for keyword: '{book_title}'.")
        return

    # 4. If multiple matches, show a table and prompt selection
    chosen_book = None

    if len(matches) == 1:
        chosen_book = matches[0]

    print(f"{len(matches)} match(es) found for '{book_title}':")
    print(f"{'No.':^5} {'Title':^40} {'Author':^20} {'Year':^6} {'Copies':^8}")
    print("-" * 85)

    for i, b in enumerate(matches, start=1):
        print(f"{i:^5} {str(b.get('Title',''))[:40]:^40} "
            f"{str(b.get('Author',''))[:20]:^20} "
            f"{str(b.get('Year','')):^6} "
            f"{str(b.get('Copies','')):^8}")

    if len(matches) > 1:
        while True:
            choice = input("Enter the No. of the book to borrow (or 0 to cancel): ").strip()
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            num = int(choice)
            if num == 0:
                print("Borrow cancelled.")
                return
            if 1 <= num <= len(matches):
                chosen_book = matches[num - 1]
                break
            print(f"Please select a number between 1 and {len(matches)}, or 0 to cancel.")

    # 5. Inventory check
    copies = int(chosen_book.get("Copies", 0))

    if copies <= 0:
        print(f"Error: No available copies of '{chosen_book.get('Title','')}'.")
        return

    # 6 Prevent duplicate borrow
    title_lower = str(chosen_book.get("Title", "")).lower()
    already_has = any(
        isinstance(entry, dict) and str(entry.get("Book Title", "")).lower() == title_lower
        for entry in user["BooksBorrowed"]
    )
    if already_has:
        print(f"Error: User {user_id.upper()} already has '{chosen_book.get('Title','')}' borrowed.")
        return

    # 7. Compute due date 
    due_date = (datetime.today() + timedelta(days=14)).date().isoformat()

    # 8. Update user & catalogue
    user["BooksBorrowed"].append({
        "Book Title": chosen_book.get("Title", ""),
        "Due Date": due_date
    })
    chosen_book["Copies"] = copies - 1

    # 9. Confirmation 
    print(f"'{chosen_book.get('Title','')}' borrowed by {user.get('Name','')} (ID: {user_id.upper()}). Due on {due_date}.")

def return_book(users: List[dict], catalogue: List[dict], user_id: str, book_title: str, return_date: str) -> None:
    """
    Return a borrowed book for a user, update fines and inventory, and confirm the outcome.

    Args:
        users (List[dict]): List of user dictionaries containing
                            (ID, Name, Email, Address, Fine, BooksBorrowed).
        catalogue (List[dict]): List of book dictionaries containing
                                (Title, Author, Year, ISBN, Copies).
        user_id (str): The ID of the user returning the book (case-insensitive).
        book_title (str): Keyword to match the borrowed book title (case-insensitive).
        return_date (str): The date the book is returned in YYYY-MM-DD format.

    Returns:
        None

    Notes:
        - Prints errors for: unknown user, no borrowed books, empty keyword,
          no title match, or invalid date formats.
        - If multiple matches are found, displays a table and prompts the user
          to select which book to return.
        - Computes a late fine at $2.00 per day past the due date and adds it to
          the user's Fine.
        - Removes the returned book from the user's BooksBorrowed and increments
          the corresponding catalogue Copies.
    """
    # 1. Find user
    user = next((u for u in users if u.get("ID") == user_id.upper()), None)
    if not user:
        print(f"Error: No user found with ID {user_id}.")
        return
    
    # 2. Check the user's borrowed books
    borrowed = user["BooksBorrowed"]
    if not borrowed:
        print(f"Error: User {user_id} has no borrowed books.")
        return

    # 3. Keyword match within user's borrowed list (case-insensitive)
    search_term = book_title.strip().lower()

    if not search_term:
        print("Error: Search keyword cannot be empty.")
        return
    
    matches = [b for b in borrowed if search_term in str(b.get("Book Title", "")).lower()]

    if not matches:
        print(f"No borrowed books matched the keyword '{book_title}'.")
        return

    # 4. If multiple matches, show table and prompt which to return
    if len(matches) > 1:
        print(f"{len(matches)} borrowed books match '{book_title}':")
        print(f"{'No.':^5} {'Title':^40} {'Due Date':^15}")
        print("-" * 65)
        for i, b in enumerate(matches, start=1):
            print(f"{i:^5} {str(b.get('Book Title',''))[:40]:^40} {str(b.get('Due Date','')):^15}")

        while True:
            s = input("Enter the No. of the book to return (or 0 to cancel): ").strip()
            if not s.isdigit():
                print("Please enter a number.")
                continue
            n = int(s)
            if n == 0:
                print("Return cancelled.")
                return
            if 1 <= n <= len(matches):
                chosen = matches[n - 1]
                break
            print(f"Please select a number between 1 and {len(matches)}, or 0 to cancel.")
    else:
        chosen = matches[0]
        print("1 borrowed book matched:")
        print(f"{'No.':^5} {'Title':^40} {'Due Date':^15}")
        print("-" * 65)
        print(f"{1:^5} {str(chosen.get('Book Title',''))[:40]:^40} {str(chosen.get('Due Date','')):^15}")

    # 5. Parse dates
    due_str = chosen.get("Due Date", "")
    try:
        due_dt = datetime.strptime(due_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"Error: Stored due date '{due_str}' is invalid.")
        return

    try:
        ret_dt = datetime.strptime(return_date.strip(), "%Y-%m-%d").date()
    except ValueError:
        print(f"Error: Return date '{return_date}' is invalid. Use YYYY-MM-DD.")
        return

    # 6. Compute late days and fine ($2/day)
    late_days = (ret_dt - due_dt).days
    added_fine = 0.0
    if late_days > 0:
        added_fine = 2.0 * late_days
        try:
            user["Fine"] = float(user.get("Fine", 0.0)) + added_fine
        except (TypeError, ValueError):
            user["Fine"] = added_fine

    # 7. Remove from user's borrowed list 
    # Remove the exact dict object 'chosen'
    try:
        borrowed.remove(chosen)
    except ValueError:
        # Fallback: remove by matching title+due
        borrowed[:] = [b for b in borrowed if not (
            isinstance(b, dict)
            and str(b.get("Book Title","")) == str(chosen.get("Book Title",""))
            and str(b.get("Due Date","")) == str(chosen.get("Due Date",""))
        )]

    # 8. Increment catalogue copies for this title 
    title_exact = str(chosen.get("Book Title", ""))
    cat_book = next((b for b in catalogue if str(b.get("Title","")) == title_exact), None)
    if cat_book is not None:
        try:
            cat_book["Copies"] = int(cat_book.get("Copies", 0)) + 1
        except (TypeError, ValueError):
            cat_book["Copies"] = 1  # if it was invalid, reset to 1 on return

    # 9. Confirmation
    if added_fine > 0:
        print(f"Returned '{title_exact}'. Late by {late_days} day(s): fine added ${added_fine:.2f}.")
        print(f"New outstanding fine for {user['Name']} (ID: {user_id}): ${float(user['Fine']):.2f}")
    else:
        print(f"Returned '{title_exact}' on time. No fines added.")