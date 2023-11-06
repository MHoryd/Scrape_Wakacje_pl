from flask import Flask
from config import Config
from app.extensions import db, migrate, scheduler
from scrape_script.task import task

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app,db)
    scheduler.init_app(app)

    with app.app_context():
        # Register blueprints here
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)
        from app.list import bp as list_bp
        app.register_blueprint(list_bp)
        from app.insert import bp as insert_bp
        app.register_blueprint(insert_bp)



        # Start the scheduler and scrape script
        scheduler.start()
        # scheduler.remove_all_jobs()
        if len(scheduler.get_jobs()) == 0:
            scheduler.add_job(id='Scrape_script', func=task)

        # Update the list of countries in db
        from helpers.countries_getter import update_country
        update_country()

    return app