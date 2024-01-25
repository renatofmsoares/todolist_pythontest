from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurations, extensions, and other setup can be added here

    # Import and register blueprints (if any)
    from .routes import bp as tasks_blueprint
    app.register_blueprint(tasks_blueprint)

    return app
