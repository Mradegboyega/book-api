from typing import Optional, List
from uuid import UUID
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()

# Define Pydantic models for book data
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int
    language: str

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str

class BookUpdate(BaseModel):
    title: str
    pages: int

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[Book | List[Book]] = None

# Dictionary to store books with UUID as keys
books: dict[str, Book] = {}

# Home route
@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return Response(message="Hello from the books API")

# Get all books
@app.get("/books", status_code=status.HTTP_200_OK, response_model=Response)
def get_books():
    return Response(data=list(books.values()))

# Get a book by its ID
@app.get("/book/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return Response(data=book)

# Add a new book
@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=Response)
def add_book(book_in: BookCreate):
    new_book = Book(id=str(UUID(int=len(books) + 1)), **book_in.dict())
    books[new_book.id] = new_book
    return Response(message="Book added successfully", data=new_book)

# Update an existing book
@app.put("/books/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    book.title = book_in.title
    book.pages = book_in.pages

    return Response(message="Book updated successfully", data=book)

# Delete a book by its ID
@app.delete("/books/{id}", response_model=Response)
def delete_book(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    del books[book.id]

    return Response(message="Book deleted successfully")
