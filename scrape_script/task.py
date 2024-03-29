from app.extensions import scheduler, db
from app.models.search_params import Search_param
from scrape_script.script_main import ScrapeControler


def task():
    list_to_execute = []
    with scheduler.app.app_context():
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
                "departure_city": param_result.departure_city,
                "rating": param_result.rating
                }
            list_to_execute.append(param)
        if list_to_execute:
            SC = ScrapeControler(list_to_execute)
            SC.run()