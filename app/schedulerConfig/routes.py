from app.schedulerConfig import bp
from flask import render_template
from app.extensions import scheduler

@bp.route('/schedulerConfig')
def schedulerConfig():
    with scheduler.app.app_context():
        jobs_list = scheduler.get_jobs()
    return render_template('schedulerConfig.html', jobs_list = jobs_list)