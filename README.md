# Late Night Show API
A RESTful Flask API backend for managing late night show episodes, guests, and their appearances with ratings. Includes user authentication with JWT.

## Features
- User registration and login with JWT authentication
- CRUD operations for Episodes, Guests, Appearances
- Validation for appearance ratings (1 to 5)
- Relationships between guests, episodes, and appearances
- Secure password hashing

## Technologies Used
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL (or any SQL database supported by SQLAlchemy)
- Werkzeug Security for password hashing

## Installation
1. Clone the repository
git clone 
cd late-show-api

2. Create and activate a virtual environment
       ```bash
  python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file with your database URL and JWT secret key:
   ```bash
   DATABASE_URL=postgresql://username:password@localhost:5432/your_db
   JWT_SECRET_KEY=your_jwt_secret
Initialize the database
flask db upgrade

6. Run the server

      ```bash
      flask run
```
## API Endpoints

## Authentication

POST /register — Register a new user

POST /login — Login and get JWT token

## Episodes
GET /episodes — List all episodes

GET /episodes/ — Get episode details including appearances

DELETE /episodes/ — Delete an episode (protected route)

Guests GET /guests — List all guests

Appearances POST /appearances — Create an appearance with rating (protected route)

Usage Notes Use the JWT access token from /login in the Authorization header as: Authorization: Bearer <access_token>

Appearance ratings must be integers between 1 and 5.

## License
 MIT License

## Author
Alicia 