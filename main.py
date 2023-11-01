from flask import Flask, render_template,redirect,current_app
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, DateField,SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Scrape_script.script_main import ScrapeControler
import os


app = Flask(__name__)
path = os.path.join(os.getcwd(),"Database_instance/scrape_database.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}'
app.config['SECRET_KEY'] = os.environ.get('Flask_app_secret_key')
db= SQLAlchemy(app)
migrate = Migrate(app, db)
scheduler = APScheduler()
   

class Search_param(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(60),nullable=False)
    date_from = db.Column(db.String(60),nullable=False)
    date_to = db.Column(db.String(60),nullable=False)
    stay_length = db.Column(db.String(60),nullable=False)
    stars = db.Column(db.String(60),nullable=False)
    max_price = db.Column(db.String,nullable=False)
    transportation = db.Column(db.String(60),nullable=False)
    amenities = db.Column(db.String(60),nullable=False)
    departure_city = db.Column(db.String(60),nullable=False)


class New_param_form(FlaskForm):
    country = StringField(label="Country to search in", validators=[DataRequired()])
    date_from = DateField(label="Date from", validators=[DataRequired()])
    date_to = DateField(label="Date to", validators=[DataRequired()])
    stay_length = StringField(label="Length of stay to search for. For exampele format: 1 to 10 days (in format 1-10)", validators=[DataRequired()])
    stars = SelectField(label="Hotel star count. From 2 to 5",choices=[("2-gwiazdkowe",2),("3-gwiazdkowe",3),("4-gwiazdkowe",4), ("5-gwiazdkowe",5)], validators=[DataRequired()])
    max_price = IntegerField(label="Max price for both", validators=[DataRequired()])
    transportation = SelectField(label="Hotel star count. From 2 to 5",choices=[("samolotem","Samolot"),("samochodem","Dojazd własny"),("autokarem","Autokar")], validators=[DataRequired()])
    amenities = SelectField(label="Amenities options", choices=[("all-inclusive","all-inclusive"),("HB","Śniadania i obiadokolacje"),("BB","Śniadania"),("wlasne","Brak"),("ZO","Wg. Programu"),("FB","Trzy posiłki")], validators=[DataRequired()])
    departure_city = SelectField(label="Start city", choices=[("z-gdanska","Gdańsk"),("z-katowic","Katowice"),("z-krakowa","Kraków"),("z-warszawy","Warszawa"),("z-wroclawia","Wrocław")], validators=[DataRequired()])
    submit = SubmitField(label="Submit")

@app.route("/")
def home():
    params_count = Search_param.query.count()

    return render_template('home.html',params_count=params_count)

@app.route("/list")
def list():
    params_list = db.session.execute(db.select(Search_param)).scalars()
    return render_template('list.html', params_list=params_list)


@app.route("/insert",methods=['GET',"POST"])
def insert():
    form = New_param_form()
    if form.validate_on_submit():
        new_param = Search_param(
            country = form.country.data,
            date_from = form.date_from.data,
            date_to = form.date_to.data,
            stay_length = form.stay_length.data,
            stars = form.stars.data,
            max_price = form.max_price.data,
            transportation = form.transportation.data,
            amenities = form.amenities.data,
            departure_city = form.departure_city.data
        )
        db.session.add(new_param)
        db.session.commit()
        return redirect("/list")
    return render_template('insert.html',form=form)

@app.route("/execute_code", methods=['POST'])
@scheduler.task('cron', id='1', hour=18)
def task():
    list_to_execute = []

    with app.app_context():
        all_params_to_execute = db.session.execute(db.select(Search_param)).scalars()
        for param_result in all_params_to_execute:
            param = {
                "country": param_result.country,
                "date_from": param_result.date_from,
                "date_to": param_result.date_to,
                "stay_length": param_result.stay_length,
                "stars": param_result.stars,
                "max_price": param_result.max_price,
                "transportation": param_result.transportation,
                "amenities": param_result.amenities,
                "departure_city": param_result.departure_city
            }
            list_to_execute.append(param)
        if len(list_to_execute) > 0:
            SC = ScrapeControler(list_to_execute)
            SC.run()
    return redirect('/')

@app.route('/delete/<int:paramid>', methods=['DELETE'])
def delete_param(paramid):
    param_to_delete = db.get_or_404(Search_param, paramid)
    db.session.delete(param_to_delete)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    scheduler.start()
    app.run(host='0.0.0.0')
    app.run(debug=False)

