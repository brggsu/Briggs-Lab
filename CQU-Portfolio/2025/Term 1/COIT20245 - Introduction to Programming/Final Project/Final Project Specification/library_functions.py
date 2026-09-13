from typing import List, Optional
import csv
from datetime import datetime, timedelta

# ---------------------------
# Phase 1: Book Catalogue
# ---------------------------

def load_catalogue(filename) -> List[dict]:
    pass # Write your code here

def save_catalogue(filename, catalogue) -> None:
    pass # Write your code here

def add_book(catalogue, title, author, year, isbn, copies) -> None:
    pass # Write your code here

def display_books(booklist) -> None:
    pass # Write your code here

def search_by_title(catalogue, keyword) -> List[dict]:
    pass # Write your code here

def search_by_author(catalogue, author) -> List[dict]:
    pass # Write your code here

def sort_by_title(catalogue) -> None:
    pass # Write your code here

def sort_by_year(catalogue) -> None:
    pass # Write your code here

# ---------------------------
# Phase 2: Library Users
# ---------------------------

def load_users(filename) -> List[dict]:
    pass # Write your code here

def save_users(filename, users) -> None:
    pass # Write your code here

def register_user(users, name, email, address) -> str:
    pass # Write your code here

def display_user_details(users, library_id) -> None:
    pass # Write your code here

def pay_fine(users, library_id) -> None:
    pass # Write your code here

def borrow_book(users, catalogue, library_id, book_title) -> None:
    pass # Write your code here

def return_book(users, catalogue, library_id, book_title, return_date_str) -> None:
    pass # Write your code here