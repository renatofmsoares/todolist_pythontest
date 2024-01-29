import pdb
from flask import render_template, Blueprint

from app.tasks_module.models import Task

main_blueprint = Blueprint("main_module", __name__,
    template_folder='templates',
    static_folder='static')


