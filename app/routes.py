# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task

bp = Blueprint('tasks', __name__)

# Dummy data (replace with actual data or database integration)
tasks = [
    Task(1, 'Task 1', 'Description for Task 1'),
    Task(2, 'Task 2', 'Description for Task 2'),
    Task(3, 'Task 3', 'Description for Task 3'),
]

@bp.route('/')
def index():
    print("Entering the index route...")  # Check if this print statement is displayed
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['GET'])
def add_task_form():
    return render_template('add_task.html')

@bp.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')

    # Generate a unique ID (replace with database ID)
    task_id = len(tasks) + 1 if tasks else 1

    new_task = Task(task_id, title, description)
    tasks.append(new_task)

    return redirect(url_for('tasks.index'))
