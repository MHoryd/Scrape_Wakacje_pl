from flask import Blueprint

bp = Blueprint('insert', __name__)

from app.insert import routes