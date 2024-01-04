# NoteX
This is a simple noteX app that support the following  functionalities:

**Authentication Endpoints:**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


POST/api/auth/signup.
POST/api/auth/login.
Note Endpoints: GET /api/notes.
GET/api/notes/:id.
POST/api/notes, 
PUT/api/notes/:id,
DELETE/api/notes/:id, POST/api/notes/:id/share, GET/api/search?q=:query
Database: SQL
Rate Limiting and Request Throttling
Search Functionality: GET/api/search?q=:query
Unit Tests and Integration Tests

**Requirements**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
All requirement has been listed in Requirement.txt


**Installation**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Clone the repository
git clone (https://github.com/manas608/NoteX.git)
Install Dependencies
cd django-NoteX
pip install -r requirements.txt
Create a file names .env in the folder where your settings.py file is present. Enter following information in your .env file
SECRET_KEY=<your_secret_key>
Run django migrations
python manage.py migrate
Run django server
python manage.py runserver

