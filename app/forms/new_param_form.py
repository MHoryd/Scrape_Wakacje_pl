from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, DateField,SelectField, IntegerField
from wtforms.validators import DataRequired


class New_param_form(FlaskForm):
    country = StringField(label="Country", validators=[DataRequired()])
    date_from = DateField(label="Date from", validators=[DataRequired()])
    date_to = DateField(label="Date to", validators=[DataRequired()])
    stay_length = StringField(label="Length of stay to search for. For example format: 1 to 10 days (in format 1-10)", validators=[DataRequired()])
    stars = SelectField(label="Hotel star count. From 2 to 5",choices=[("2-gwiazdkowe",2),("3-gwiazdkowe",3),("4-gwiazdkowe",4), ("5-gwiazdkowe",5)], validators=[DataRequired()])
    max_price = IntegerField(label="Max price for both", validators=[DataRequired()])
    transportation = SelectField(label="Hotel star count. From 2 to 5",choices=[("samolotem","Samolot"),("samochodem","Dojazd własny"),("autokarem","Autokar")], validators=[DataRequired()])
    amenities = SelectField(label="Amenities options", choices=[("all-inclusive","all-inclusive"),("HB","Śniadania i obiadokolacje"),("BB","Śniadania"),("wlasne","Brak"),("ZO","Wg. Programu"),("FB","Trzy posiłki")], validators=[DataRequired()])
    departure_city = SelectField(label="Start city", choices=[("z-gdanska","Gdańsk"),("z-katowic","Katowice"),("z-krakowa","Kraków"),("z-warszawy","Warszawa"),("z-wroclawia","Wrocław")], validators=[DataRequired()])
    submit = SubmitField(label="Submit")