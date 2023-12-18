from fastapi import FastAPI, Response
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

# Create a FastAPI app instance
app = FastAPI()

# Data model for the book resource using Pydantic
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int
    language: str

# Input model for creating a new book
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str

# Input model for updating an existing book
class BookUpdate(BaseModel):
    title: str
    pages: int

# Response model for a list of books
class Books(BaseModel):
    books: list[Book]

# Dictionary to store books with UUID as keys
books: dict[str, Book] = {}

# Home route
@app.get("/")
def home():
    return {"message": "Hello from the books API"}

# Get all books
@app.get("/books", response_model=Books)
def get_books():
    return Books(books=list(books.values()))

# Get a book by its ID
@app.get("/books/{id}", response_model=Book)
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}

    return book

# Add a new book
@app.post("/books", response_model=Response, status_code=201)
def add_book(book_in: BookCreate):
    book = Book(
        id=str(UUID(int=len(books) + 1)),
        **book_in.dict(),
    )
    books[book.id] = book
    return Response(content=book)

# Update an existing book
@app.put("/books/{id}", response_model=Response)
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}

    book.title = book_in.title
    book.pages = book_in.pages

    return Response(message="Book updated successfully", content=book)

# Delete a book by its ID
@app.delete("/books/{id}", response_model=Response)
def delete_book(id: UUID):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}

    del books[book.id]

    return Response(message="Book deleted successfully")
