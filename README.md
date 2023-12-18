FastAPI Books API
Overview

This is a simple FastAPI application that provides basic CRUD (Create, Read, Update, Delete) operations for managing a collection of books. The application uses Pydantic for data validation and FastAPI for building the API endpoints.
Installation

    Clone the Repository:

    bash

git clone https://github.com/Mradegboyega/fastapi-books-api.git
cd fastapi-books-api

Usage
Run the FastAPI Application:

bash

uvicorn main:app --reload

This will start the FastAPI development server, and you can access the API at http://127.0.0.1:8000.
Endpoints:

    Home:
        URL: http://127.0.0.1:8000/
        Method: GET
        Description: Returns a welcome message.

    Get All Books:
        URL: http://127.0.0.1:8000/books
        Method: GET
        Description: Returns a list of all books.

    Get Book by ID:
        URL: http://127.0.0.1:8000/books/{id}
        Method: GET
        Description: Returns details of a specific book based on its ID.

    Add a Book:
        URL: http://127.0.0.1:8000/books
        Method: POST
        Description: Adds a new book to the collection.

    Update a Book:
        URL: http://127.0.0.1:8000/books/{id}
        Method: PUT
        Description: Updates details of a specific book based on its ID.

    Delete a Book:
        URL: http://127.0.0.1:8000/books/{id}
        Method: DELETE
        Description: Deletes a specific book based on its ID.

Response Format:

The API responses follow a standardized format:

json

{
  "message": "Operation success message",
  "has_error": false,
  "error_message": "Error details (if any)",
  "data": "Response data (if any)"
}

Contributing

If you find any issues or have improvements to suggest, please feel free to open an issue or create a pull request.