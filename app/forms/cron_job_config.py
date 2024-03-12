from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField,SubmitField
from wtforms.validators import DataRequired


class CronJobConfig(FlaskForm):
    enable_job = BooleanField(label="Enable Job")
    hour = SelectField(label="Hour", choices=[(str(i),str(i)) for i in range(24)],validators=[DataRequired()])
    minute = SelectField(label="Minute", choices=[(str(i),str(i)) for i in range(60)],validators=[DataRequired()])
    submit = SubmitField('Submit')