import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('Flask_app_secret_key')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('Flask_app_db_url')
    STATIC_URL_PATH = 'static'
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')