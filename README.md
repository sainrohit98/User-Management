# Flask User Management API

This is a simple Flask application that manages a list of users. The application provides a RESTful API for retrieving, adding, updating, and deleting users. Additionally, a background thread automatically updates the status of the first three users every 5 minutes. The application also uses AJAX to dynamically update the user status in the front-end.

## Features

- Retrieve all users
- Retrieve a single user by ID
- Add a new user
- Update an existing user's information
- Delete a user
- Automatically update the status of the first three users after 5 minutes
- CORS enabled for cross-origin requests
- Dynamic status updates on the front-end using AJAX

## Requirements

- Python 3.x
- Flask
- Flask-CORS

## Installation


1. Clone the repository:
   ```bash
   git clone https://github.com/sainrohit98/User-Management.git

2. create and activate a virtual environment:
python -m venv venv 
venv\Scripts\activate



3.Install the required dependencies:
pip install -r requirements.txt


4.Run the Flask application:
python app.py




### API Endpoints
1. Get All Users
Endpoint: /users
Method: GET

Returns a list of all users.

Response:

[
    {"id": 1, "name": "Alice", "status": "Busy"},
    {"id": 2, "name": "Bob", "status": "Busy"},
    {"id": 3, "name": "Charlie", "status": "Busy"},
    {"id": 4, "name": "David", "status": "Busy"},
    {"id": 5, "name": "Eve", "status": "Busy"}
]
2. Get a Single User by ID
Endpoint: /users/<int:user_id>
Method: GET

Retrieves a specific user by their ID.

Response:
json
{
    "id": 1,
    "name": "Alice",
    "status": "Busy"
}
3. Add a New User
Endpoint: /users
Method: POST

Adds a new user to the system. The request body must contain the user's name and status.

Request Body:
json
{
    "name": "John",
    "status": "Available"
}
Response:
json

{
    "id": 6,
    "name": "John",
    "status": "Available"
}
4. Update a User
Endpoint: /users/<int:user_id>
Method: PUT

Updates the details of an existing user.

Request Body:
json

{
    "name": "Alice",
    "status": "Available"
}
Response:
json

{
    "id": 1,
    "name": "Alice",
    "status": "Available"
}
5. Delete a User
Endpoint: /users/<int:user_id>
Method: DELETE

Deletes a specific user by their ID.

Response:

204 No Content
