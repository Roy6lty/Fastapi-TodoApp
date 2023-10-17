# Description
This project uses the fastapi framework to build a todoapp 

# features
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

![alt text](https://github.com/[olowoleru06@gmil.com]/[Fastapi-TodoApp]/blob/[main]/edit.png?raw=true)
![Alt text](./static/todo/todo-img/edit.png?raw=true "edit Todo")