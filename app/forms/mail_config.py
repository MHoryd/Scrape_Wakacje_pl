from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class MailConfig(FlaskForm):
    notification_email= StringField(label='Sender email', validators=[DataRequired(), Length(max=100)])
    notification_receivers_email= StringField(label='Receiver emails', validators=[DataRequired(),Length(max=100)])
    notification_pass= StringField(label='Sender email pass', validators=[DataRequired(),Length(max=100)])
    notification_smtp_server= StringField(label='SMTP Server', validators=[DataRequired(),Length(max=100)])
    submit = SubmitField('Submit')