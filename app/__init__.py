from flask import Flask
from app.main_module.views import main_blueprint
from app.tasks_module.views import tasks_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(tasks_blueprint)

    for rule in app.url_map.iter_rules():
        print(rule)

    return app
