from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task

bp = Blueprint('tasks', __name__)

# Dummy data (replace with actual data or database integration)
tasks = [
    Task('Task 1', 'Description for Task 1'),
    Task('Task 2', 'Description for Task 2'),
    Task('Task 3', 'Description for Task 3'),
]

@bp.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['GET'])
def add_task_form():
    return render_template('add_task.html')

@bp.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('task-title-input')
    description = request.form.get('task-description-input')

    new_task = Task(title, description)

    tasks.append(new_task)
    print(new_task.__getstate__())

    return redirect(url_for('tasks.index'))
