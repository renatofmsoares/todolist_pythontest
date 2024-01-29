from flask import render_template, Blueprint
from flask import request, redirect, url_for

from app.tasks_module.models import Task

tasks_blueprint = Blueprint("tasks_module", __name__,
    template_folder='templates',
    static_folder='static')

# Dummy data (replace with actual data or database integration)
tasks = [
    Task('Task 1', 'Description for Task 1'),
    Task('Task 2', 'Description for Task 2'),
    Task('Task 3', 'Description for Task 3'),
]

@tasks_blueprint.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@tasks_blueprint.route('/add_task', methods=['GET'])
def add_task_form():
    return render_template('add_task.html')

@tasks_blueprint.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('task-title-input')
    description = request.form.get('task-description-input')

    new_task = Task(title, description)

    tasks.append(new_task)
    print(new_task.__getstate__())

    return render_template('index.html', tasks=tasks)

