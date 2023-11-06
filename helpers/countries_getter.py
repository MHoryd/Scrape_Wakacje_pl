import requests
from app.extensions import db
from app.models.destinations import Destinations

def update_country():
    request = requests.get("https://www.wakacje.pl/v2/api/countries")
    response = request.json()
    countries_from_wakacje_response = [(country['urlName'],country['label']) for country in response['data']]
    countries_from_app_db = Destinations.query.all()
    countries_from_app_list = [(i.country, i.country_label) for i in countries_from_app_db]
    
    new_elem_from_wakacje_api = [country for country in countries_from_wakacje_response if country not in countries_from_app_list]
    obsolete_elem_in_app_db = [country for country in countries_from_app_list if country not in countries_from_wakacje_response]

    if new_elem_from_wakacje_api:
        object_to_inser = [Destinations(country=country[0],country_label=country[1]) for country in new_elem_from_wakacje_api]
        db.session.add_all(object_to_inser)
        db.session.commit()

    if obsolete_elem_in_app_db:
        for object in obsolete_elem_in_app_db:
            instance = db.session.execute(db.select(Destinations).filter_by(country=object[0])).scalar_one()
            db.session.delete(instance)
            db.session.commit()

    return [(country.country, country.country_label) for country in Destinations.query.all()]