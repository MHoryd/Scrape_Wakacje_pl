from flask import render_template, redirect, request
from app.insert import bp
from app.forms.new_param_form import New_param_form
from app.extensions import db
from app.models.search_params import Search_param
from helpers.countries_getter import update_country


@bp.route('/insert',methods=['GET',"POST"])
def insert_new_param():
    form = New_param_form()
    form.country.choices = update_country()
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
