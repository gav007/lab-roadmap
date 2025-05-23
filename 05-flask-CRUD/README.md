# Flask CRUD App with SQLite

## Overview

This is a simple Flask web application demonstrating basic **CRUD** (Create, Read, Update, Delete) functionality using an **SQLite** database.

Users can submit feedback entries, which are saved to the database and displayed on the homepage.

This project covers:

- Setting up a Flask app  
- Connecting to a SQLite database  
- Creating database tables with SQL schema  
- Reading and writing data from/to the database  
- Using HTML templates with Jinja2 for dynamic content  
- Handling GET and POST requests with forms  

---

## Project Structure

lab04-flask-crud/
├── app.py # Main Flask application code
├── schema.sql # SQL commands to create database tables
├── requirements.txt # Python dependencies (Flask)
├── app.db # SQLite database file (auto-created)
├── templates/ # HTML templates for pages
│ ├── base.html # Base template layout
│ ├── index.html # Home page (list feedback)
│ ├── create.html # Form page to add feedback
├── env/ # Python virtual environment (not committed)

yaml
Copy code

---

## Cloning and Running the Project

If you want to **clone this project** from GitHub and run it locally, follow these steps:

### 1. Clone the repository

Open your terminal or Git Bash and run:

```
git clone https://github.com/yourusername/lab04-flask-crud.git
Replace yourusername and repo name with the actual URL if different.

2. Navigate into the project folder

cd lab04-flask-crud
3. Create and activate a virtual environment
Create a Python virtual environment to keep dependencies separate:


python -m venv env
Activate the environment:

On Windows PowerShell:



.\env\Scripts\Activate.ps1
On Git Bash or Command Prompt:



.\env\Scripts\activate
4. Install dependencies
With the virtual environment activated, install required packages:


pip install -r requirements.txt
5. Run the Flask app
Start the application with:


python app.py
6. Open your browser
Go to:



http://127.0.0.1:5000/