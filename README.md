# RestfulApi_python
Task Management RESTful API
This project is a simple yet robust RESTful API for a Task Management system, built with Python using the FastAPI framework. It demonstrates core backend development concepts including CRUD operations, database integration, data validation, and automated API documentation.

Features
Create, Read, Update, Delete (CRUD) operations for tasks.

Data Validation using Pydantic to ensure data integrity.

Database Integration with SQLite through the SQLAlchemy ORM.

Automated API Documentation provided by Swagger UI and ReDoc.

Asynchronous support thanks to FastAPI and Starlette.

Tech Stack
Language: Python 3.9+

Framework: FastAPI

Database ORM: SQLAlchemy

Data Validation: Pydantic

Server: Uvicorn

Database: SQLite

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.7+

pip package manager

Installation & Setup
Clone the repository:

git clone https://github.com/Bristiii/RestfulApi_python.git
cd RestfulApi_python

Create and activate a virtual environment:

On Windows:

python -m venv venv
venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file yet, you can create one by running pip freeze > requirements.txt after installing the packages manually with pip install "fastapi[all]" sqlalchemy)

Running the Application
Once the setup is complete, you can run the API server using Uvicorn:

uvicorn main:app --reload

The --reload flag enables hot-reloading, which automatically restarts the server whenever you make changes to the code.

The API will be available at http://127.0.0.1:8000.

API Documentation
FastAPI automatically generates interactive API documentation. Once the server is running, you can access it at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

You can use the Swagger UI to view all available endpoints and test them directly from your browser.

API Endpoints
Here is a summary of the available API endpoints:

Method

Endpoint

Description

Request Body Example

Success Response (200 OK)

POST

/tasks/

Create a new task.

{"title": "Learn FastAPI", "description": "Read docs"}

{"id": 1, "title": "Learn FastAPI", "description": "Read docs", "completed": false}

GET

/tasks/

Retrieve a list of all tasks.

N/A

[{"id": 1, ...}, {"id": 2, ...}]

GET

/tasks/{task_id}

Retrieve a single task by ID.

N/A

{"id": 1, "title": "Learn FastAPI", "description": "Read docs", "completed": false}

PUT

/tasks/{task_id}

Update an existing task.

{"title": "Master FastAPI", "completed": true}

{"id": 1, "title": "Master FastAPI", "description": "Read docs", "completed": true}

DELETE

/tasks/{task_id}

Delete a task by ID.

N/A

{"id": 1, "title": "Master FastAPI", "description": "Read docs", "completed": true}

Error Handling
If a task_id is not found, the API will return a 404 Not Found error with a detail message.

If the request body for POST is invalid (e.g., missing a title), the API will return a 422 Unprocessable Entity error with details on the validation failure.
