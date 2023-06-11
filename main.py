from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import enum
import datetime
import json


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(180))
    description=db.Column(db.String(500))
    status=db.Column(db.String(100))
    due_date=db.Column(db.DateTime)

    def __init__(self, title, description, status, due_date):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

class TaskSchema(ma.Schema):
    class Meta:
        fields=('id', 'title', 'description', 'status', 'due_date')

task_schema= TaskSchema()
tasks_schema = TaskSchema(many=True)

#To Create task 
@app.route('/task', methods=['POST'])
def add_task():
    try:
        title = request.json['title']
        description = request.json['description']
        status = request.json['status']
        due_date = request.json['due_date']
        new_task=Task(title, description, status, due_date)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.jsonify(new_task)
    except:
        return {"Status" : "Error"}

#To Get list of all tasks
@app.route('/task',methods=['GET'])
def get_all_tasks():
    try:
        all_tasks = Task.query.all()
        result = tasks_schema.dump(all_tasks)
        return jsonify(result)
    except:
        return {"Status" : "Error"}

#Get task by ID
@app.route('/task/<id>',methods=['GET'])
def get_task_by_id(id):
    try:
        task = Task.query.get(id)
        return task_schema.jsonify(task)
    except:
        return {"Status" : "Error"}


#Update Task
@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    try:
        task = Task.query.get(id)
        title = request.json['title']
        description = request.json['description']
        status = request.json['status']
        due_date = request.json['due_date']
        task.title = title
        task.description = description
        task.status = status
        task.due_date = due_date
        db.session.commit()
        return task_schema.jsonify(task)
    except:
        return {"Status" : "Error"}


#Delete Task
@app.route('/task/<id>', methods=['DELETE'])
def delete_task_by_id(id):
    try:
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return {"status" : "Success"}
    except:
        return {"Status" : "Error"}


if __name__ == '__main__':
    app.run(debug=True, port=5000)