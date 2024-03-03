from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, DateField,SelectField, IntegerField
from wtforms.validators import DataRequired
from datetime import date, timedelta

class New_param_form(FlaskForm):
    today = date.today()
    future_date = today + timedelta(days=7)
    country = SelectField(label="Country",choices=None, validators=[DataRequired()])
    date_from = DateField(label="Date from",default=today, validators=[DataRequired()])
    date_to = DateField(label="Date to",default=future_date, validators=[DataRequired()])
    stay_length_slider = StringField(label="Length of stay to search for",default="1-28", validators=[DataRequired()])
    stars = SelectField(label="Hotel star count. From 2 to 5",choices=[("2-gwiazdkowe",2),("3-gwiazdkowe",3),("4-gwiazdkowe",4), ("5-gwiazdkowe",5)], validators=[DataRequired()])
    max_price = IntegerField(label="Max price for both", default='4000', validators=[DataRequired()])
    transportation = SelectField(label="Hotel star count. From 2 to 5",choices=[("samolotem","Samolot"),("samochodem","Dojazd własny"),("autokarem","Autokar")], validators=[DataRequired()])
    amenities = SelectField(label="Amenities options", choices=[("all-inclusive","all-inclusive"),("HB","Śniadania i obiadokolacje"),("BB","Śniadania"),("wlasne","Brak"),("ZO","Wg. Programu"),("FB","Trzy posiłki")], validators=[DataRequired()])
    departure_city = SelectField(label="Start city", choices=[("z-gdanska","Gdańsk"),("z-katowic","Katowice"),("z-krakowa","Kraków"),("z-warszawy","Warszawa"),("z-wroclawia","Wrocław")], validators=[DataRequired()])
    rating = SelectField(label="Rating",choices=[("ocena-6","6+"),("ocena-7","7+"),("ocena-8","8+"),("ocena-9","9+")], validators=[DataRequired()])
    submit = SubmitField(label="Submit")