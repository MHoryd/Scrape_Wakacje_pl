from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class MailConfig(FlaskForm):
    notification_email= StringField(label='Sender email', validators=[DataRequired(), Length(max=100)])
    notification_receivers_email= StringField(label='Receiver emails', validators=[DataRequired(),Length(max=100)])
    notification_pass= StringField(label='Mailgun api key', validators=[DataRequired(),Length(max=100)])
    notification_smtp_server= StringField(label='Mailgun api url', validators=[DataRequired(),Length(max=100)])
    submit = SubmitField('Submit')