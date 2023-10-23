# Description
This project uses the fastAPI framework to build a todo app 

# Project Description
The goal of this project is to develop a RESTful API for a todo application using FastAPI. The API will allow users to create, read, update, and delete tasks. The API will be developed using Python and FastAPI, and will use SQLite as the database. The API will be tested using Pytest and coverage.py.

# Project Objectives
- Design and develop a RESTful API using FastAPI
- Use SQLite as the database for storing tasks
- Implement CRUD operations for tasks
- Test the API using Pytest and coverage.py

# Project Deliverables
- A GitHub repository containing the source code for the API
- A detailed README file explaining how to run the API locally and how to deploy it on Heroku
- A report summarizing the project objectives, methodology, results, and conclusions


# Features
- Task Addition
- Task Removal
- Email Notification of changes
- Login and Authentication
- password retrieval

# File Structure
```bash
├── alembic
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-310.pyc
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── __pycache__
│       │   └── bb6e9aac48f5_create_phone_number_for_user_column_py.cpython-310.pyc
│       └── bb6e9aac48f5_create_phone_number_for_user_column_py.py
├── alembic.ini
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── celery.cpython-310.pyc
│   │   ├── config.cpython-310.pyc
│   │   ├── database.cpython-310.pyc
│   │   ├── mail.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── routes.cpython-310.pyc
│   │   ├── schema.cpython-310.pyc
│   │   └── todo.cpython-310.pyc
│   ├── celery.py
│   ├── config.py
│   ├── database.py
│   ├── mail.py
│   ├── models.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── auth.cpython-310.pyc
│   │   │   ├── authhtml.cpython-310.pyc
│   │   │   ├── mail.cpython-310.pyc
│   │   │   ├── todo.cpython-310.pyc
│   │   │   ├── todohtml.cpython-310.pyc
│   │   │   └── userprofile.cpython-310.pyc
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── authhtml.py
│   │   ├── todo.py
│   │   ├── todohtml.py
│   │   └── userprofile.py
│   ├── schema.py
│   └── todo.py
├── static
│   └── todo
│       ├── css
│       │   ├── base.css
│       │   └── bootstrap.css
│       └── js
│           └── todo
│               ├── bootstrap.js
│               ├── jquery-slim.js
│               └── popper.js
├── templates
│   ├── add_todo.html
│   ├── edit_todo.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── navbar.html
│   ├── register.html
│   └── verification.html
└── todo.db
```


![Alt text](./static/todo/todo-img/edit.png?raw=true "edit Todo")  ![Alt text](./static/todo/todo-img/login.png?raw=true "edit Todo")

![Alt text](./static/todo/todo-img/logout.png?raw=true "edit Todo") ![Alt text](./static/todo/todo-img/registration.png?raw=true "edit Todo")
