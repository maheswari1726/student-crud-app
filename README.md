Student Database CRUD Application

Project Overview

This project is a Student Database CRUD API developed using Python, FastAPI, SQLAlchemy, and SQLite.

It allows users to create, view, update, and delete student records through REST API endpoints. FastAPI Swagger documentation is used to test the API.

Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

Student Information

Each student record contains:

- Database ID
- Student ID
- Student Name
- Date of Birth
- Email
- Phone Number

API Endpoints

Method   |      Endpoint            |            Description
GET      |        "/"               |      Check API status
POST     |     "/students"          |      Create a student
GET      |     "/students"          |      Retrieve all students
GET      | "/students/{student_id}" |      Retrieve a student by ID
PUT      | "/students/{student_id}" |      Update a student
DELETE   | "/students/{student_id}" |      Delete a student

Installation and Setup

1. Install Python.

2. Clone or download this repository.

3. Open a terminal in the project folder.

4. Create a virtual environment:
   
   "python -m venv venv"

5. Activate the environment on Windows PowerShell:
   
   ".\venv\Scripts\Activate.ps1"

6. Install dependencies:
   
   "python -m pip install -r requirements.txt"

7. Start the server:
   
   "python -m uvicorn main:app --reload"

8. Open the API documentation:
   
   "http://127.0.0.1:8000/docs"

Database

The application uses SQLite. The database file "students.db" is created automatically when the application starts.

Testing

The API endpoints were tested using FastAPI Swagger UI. Successful requests were received for creating, retrieving, updating, and deleting student records.

Learning Outcomes

- Understanding REST API development
- Working with FastAPI and SQLAlchemy
- Performing CRUD operations
- Using SQLite for data persistence
- Testing API endpoints using Swagger UI

Author

Maheswari Nagaraju
