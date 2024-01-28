from flask import Blueprint

tasks_blueprint = Blueprint("tasks_module", __name__)

# Import views after creating the blueprint to avoid circular imports
from app.tasks_module import views