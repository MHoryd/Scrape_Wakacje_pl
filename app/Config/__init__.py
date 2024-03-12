from flask import Blueprint

bp = Blueprint('config',__name__)

from app.Config import routes