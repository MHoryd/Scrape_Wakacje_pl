from flask import Flask
from config import Config
from app.extensions import db, scheduler
from scrape_script.task import task

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    scheduler.init_app(app)

    with app.app_context():
        # Register blueprints here
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)
        from app.list import bp as list_bp
        app.register_blueprint(list_bp)
        from app.insert import bp as insert_bp
        app.register_blueprint(insert_bp)
        from app.Config import bp as scheduler_bp
        app.register_blueprint(scheduler_bp)


        # Update the list of countries in db
        from helpers.countries_getter import update_country
        update_country()

    return app