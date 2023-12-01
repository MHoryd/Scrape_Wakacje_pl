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
    form.stay_length_slider.data = '1-28'
    if request.method == 'POST' and form.validate_on_submit():
        new_param = Search_param(
            country = form.country.data,
            date_from = form.date_from.data,
            date_to = form.date_to.data,
            stay_length = form.stay_length_slider.data,
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

@bp.route('/insert/<int:paramid>',methods=['GET',"POST"])
def edit_existing_param(paramid):
    param_to_edit = db.session.query(Search_param).get(paramid)
    form = New_param_form(obj=param_to_edit)
    form.country.choices = update_country()
    if request.method == 'POST' and form.validate_on_submit():
        param_to_edit.country = form.country.data
        param_to_edit.date_from = form.date_from.data
        param_to_edit.date_to = form.date_to.data
        param_to_edit.stay_length = form.stay_length_slider.data
        param_to_edit.stars = form.stars.data
        param_to_edit.max_price = form.max_price.data
        param_to_edit.transportation = form.transportation.data
        param_to_edit.amenities = form.amenities.data
        param_to_edit.departure_city = form.departure_city.data
        db.session.commit()
        return redirect("/list")
    return render_template('insert.html',form=form)