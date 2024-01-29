from flask import Blueprint

main_blueprint = Blueprint("main_module", __name__,
    template_folder='templates',
    static_folder='static')

# Import views after creating the blueprint to avoid circular imports
from app.main_module import views