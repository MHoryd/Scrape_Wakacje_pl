from app.Config import bp
from app.forms.cron_job_config import CronJobConfig
from app.forms.mail_config import MailConfig
from flask import render_template, redirect
from scrape_script.task import task
from app.extensions import scheduler, db
from app.models.mail_config import mail_config
from sqlalchemy.exc import NoResultFound


@bp.route('/config', methods=['GET'])
def config():
    try:
        mail_configuration = mail_config.query.one()
    except NoResultFound:
        mail_configuration = None
    current_job = scheduler.get_job('daily_task')
    form_scheduler = CronJobConfig()
    form_mail = MailConfig()
    hour = None
    minute = None
    if mail_configuration:
        form_mail.notification_email.data = mail_configuration.notification_email
        form_mail.notification_receivers_email.data = mail_configuration.notification_receivers_email
        form_mail.notification_pass.data = mail_configuration.notification_pass
        form_mail.notification_smtp_server.data = mail_configuration.notification_smtp_server
    if current_job:
        for f in current_job.trigger.fields:
            if f.name == 'hour':
                hour = f
            if f.name == 'minute':
                minute = f
        form_scheduler.hour.data = str(hour)
        form_scheduler.minute.data = str(minute)
    return render_template('config.html', current_job = current_job,form_scheduler=form_scheduler,form_mail=form_mail, hour=hour, minute = minute,
                           mail_configuration=mail_configuration)


@bp.route('/process_scheduler_config', methods=['POST'])
def process_scheduler_config_form():
    form_scheduler = CronJobConfig()
    current_job = scheduler.get_job('daily_task')

    if form_scheduler.enable_job.data and not current_job:
        hour = form_scheduler.hour.data
        minute = form_scheduler.minute.data
        scheduler.add_job(id='daily_task', func=task, trigger='cron', hour=hour, minute=minute)
        scheduler.start()
        return redirect('/config')
    elif form_scheduler.enable_job.data and current_job:
        hour = form_scheduler.hour.data
        minute = form_scheduler.minute.data
        scheduler.modify_job(id='daily_task',hour=hour, minute=minute)
        return redirect('/config')
    elif not form_scheduler.enable_job.data and not current_job:
        return redirect('/config')
    else: 
        scheduler.remove_job(id='daily_task')
        scheduler.shutdown()
        return redirect('/config')

@bp.route('/process_mail_config', methods=['POST'])
def process_mail_config_form():
    form_mail = MailConfig()
    try:
        mail_config_in_db = mail_config.query.one()
        mail_config_in_db.notification_email=form_mail.data['notification_email']
        mail_config_in_db.notification_receivers_email=form_mail.data['notification_receivers_email']
        mail_config_in_db.notification_pass=form_mail.data['notification_pass']
        mail_config_in_db.notification_smtp_server=form_mail.data['notification_smtp_server']
        db.session.commit()
    except NoResultFound:
        new_mail_config = mail_config(notification_email=form_mail.data['notification_email'],notification_receivers_email=form_mail.data['notification_receivers_email'],
                                      notification_pass=form_mail.data['notification_pass'],notification_smtp_server=form_mail.data['notification_smtp_server'])
        db.session.add(new_mail_config)
        db.session.commit()
    return redirect('/config')