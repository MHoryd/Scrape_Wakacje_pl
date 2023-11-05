from app.main import bp
from flask import render_template
from app.extensions import db
from app.models.search_params import Search_param
from scrape_script.task import task
from flask import jsonify

@bp.route('/')
def index():
    params_count = db.session.query(Search_param).count()
    return render_template('index.html', params_count=params_count)


@bp.route('/trigger_script', methods=['POST'])
def trigger_script():
    try:
        result = task()
        return jsonify({'success': True, 'message': 'Script triggered successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})