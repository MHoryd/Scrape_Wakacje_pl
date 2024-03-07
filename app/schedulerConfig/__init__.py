from flask import Blueprint

bp = Blueprint('schedulerConfig',__name__)

from app.schedulerConfig import routes