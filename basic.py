from fastapi import FastAPI
from uuid import UUID

# Create a FastAPI app instance
app = FastAPI()

# Dictionary to store book data with UUID as keys
books = {}

# Template for book data
book_data = {
    "id": 0,
    "title": "",
    "author": "",
    "year": 0,
    "pages": 0,
    "language": ""
}

# Home route
@app.get("/")
def home():
    return {"message": "Hello from the book API"}

# Get a book by its ID
@app.get("/books/{id}")
def get_book_by_id(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    
    return book

# Add a new book
@app.post("/books")
def add_book(
    title: str,
    author: str,
    year: int,
    pages: int,
    language: str
):
    # Create a new book with a unique UUID as the ID
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int=len(books) + 1))
    new_book["title"] = title
    new_book["author"] = author
    new_book["year"] = year
    new_book["pages"] = pages
    new_book["language"] = language

    # Add the new book to the books dictionary
    books[new_book["id"]] = new_book

    return {"message": "Book added successfully", "data": new_book}

# Update an existing book
@app.put("/books/{id}")
def update_book(
    id: str,
    title: str,
    author: str,
    year: int,
    pages: int,
    language: str
):
    # Check if the book exists
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    
    # Update the book data
    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["pages"] = pages
    book["language"] = language

    return {"message": "Book updated successfully", "data": book}

# Delete a book by its ID
@app.delete("/books/{id}")
def delete_book(id: str):
    # Check if the book exists
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    
    # Delete the book from the dictionary
    del books[id]

    return {"message": "Book deleted successfully"}
