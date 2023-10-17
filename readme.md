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
├── con.py
├── docker-compose.yaml
├── emall
│   └── python_fastapi
│       ├── Makefile
│       ├── alembic
│       │   ├── README
│       │   ├── env.py
│       │   ├── script.py.mako
│       │   └── versions
│       │       ├── 15770e820938_created_users_table.py
│       │       ├── 1c7984990e1d_created_posts_table.py
│       │       ├── 39256113e8e5_added_verification_code.py
│       │       └── 4917da928a79_added_post_table.py
│       ├── alembic.ini
│       ├── app
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── database.py
│       │   ├── email.py
│       │   ├── main.py
│       │   ├── models.py
│       │   ├── oauth2.py
│       │   ├── routers
│       │   │   ├── auth.py
│       │   │   ├── post.py
│       │   │   └── user.py
│       │   ├── schemas.py
│       │   ├── templates
│       │   │   ├── _styles.html
│       │   │   ├── base.html
│       │   │   └── verification.html
│       │   └── utils.py
│       ├── docker-compose.yml
│       ├── readMe.md
│       └── requirements.txt
├── readme.md
├── requirements.txt
├── run.py
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