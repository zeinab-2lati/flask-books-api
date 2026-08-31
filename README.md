# Flask Books API
A simple RESTful API for managing books using Python and Flask.

# Description
This project is a simple Books API developed with Flask.
The API allows users to:
* Get all books
* Get a specific book by ID
* Add a new book
* Update an existing book
* Delete a book
The book data is currently stored in a Python list and is not connected to a database.

# Technologies
* Python
* Flask
* REST API
* JSON
* Postman
* Git
* GitHub

# API Endpoints
| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/books`      | Get all books       |
| GET    | `/books/<id>` | Get a specific book |
| POST   | `/books`      | Add a new book      |
| PUT    | `/books/<id>` | Update a book       |
| DELETE | `/books/<id>` | Delete a book       |

# Book Structure
Each book contains the following information:

```json
{
    "id": 1,
    "title": "The forty rules of love",
    "author": "elif shafak",
    "price": 500000,
    "published_year": 2000
}
```

# How to Run
## 1. Clone the repository

```bash
git clone https://github.com/zeinab-2lati/flask-books-api.git
```

## 2. Go to the project directory
```bash
cd flask-books-api
```

## 3. Install Flask
```bash
pip install flask
```

## 4. Run the application
```bash
python books.py
```

The application will run on:

```text
http://127.0.0.1:5000
```

# Testing with Postman
The API can be tested using Postman.

# Get all books
```text
GET http://127.0.0.1:5000/books
```

# Get a specific book
```text
GET http://127.0.0.1:5000/books/1
```

# Add a new book
```text
POST http://127.0.0.1:5000/books
```

Example JSON:

```json
{
    "id": 4,
    "title": "Python Programming",
    "author": "John Smith",
    "price": 600000,
    "published_year": 2026
}
```

# Update a book
```text
PUT http://127.0.0.1:5000/books/2
```

Example JSON:

```json
{
    "title": "Updated Book",
    "price": 700000
}
```

# Delete a book
```text
DELETE http://127.0.0.1:5000/books/2
```

# Project Status
This project was developed as a Flask CRUD API practice project.
Future improvements may include connecting the API to a database and adding authentication and API documentation.

