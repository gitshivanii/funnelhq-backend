# funnelhq-backend-intern-assignment

This repository contains backend intern assigment solution.

In this I have created CRUD APIs in flask as mentioned in Notion Doc.

CRUD APIs contains

```
/task (POST) => To create new task
/task (GET) => To Get List of all tasks
/task/<id> (GET) => To get task by id
/task/<id> (PUT) => To update task by id
/task/<id> (DELETE) => To delete task by id
```


To run this application follow follwing steps:

1. Clone the Repo

```
git clone https://github.com/gitshivanii/funnelhq-backend/new/backend-intern-assignment
```

2. Create virtual env

```
virtualenv venv
```

3. Activate venv

```
\path\to\env\Scripts\activate
```

3. Install Dependensies
```
pip install -r requirements.txt
```

4. Run Flask application
```
flask run
```
Note: You can also run directly from main.py by clicking run button

**5. Now to create database follow these steps**

I. Run python shell
```
  python
```
II. Import app, db 
```
  from main import db, app
```
III. Set app_context() to push
```
  app.app_context().push()
```
IV. Create all the tables
```
  db.create_all()
```

Now you can directly test APIs from postman or from Thaunder Client

Thank you!

If you face any difficulty please reach me out on mailtoshivaniparab@gmail.com


