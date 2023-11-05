from app.main import bp
from flask import render_template
from app.extensions import db
from app.models.search_params import Search_param

@bp.route('/')
def index():
    params_count = db.session.query(Search_param).count()
    return render_template('index.html', params_count=params_count)


