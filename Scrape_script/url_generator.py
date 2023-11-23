class Url_generator:


    def __init__(self, **kwarg):
        self.iteration = 0
        self.country = kwarg['country']
        self.date_from = kwarg['date_from']
        self.date_to = kwarg['date_to']
        self.stay_length = kwarg['stay_length']
        self.max_price = kwarg['max_price']
        self.transportation = kwarg['transportation']
        self.amenities = kwarg['amenities']
        self.stars = kwarg['stars']
        self.departure_city = kwarg['departure_city']
        self.url = ''


    def format_url(self):
        self.url = "https://www.wakacje.pl/wczasy/{country}/?str-{iteration},od-{date_from},do-{date_to},{stay_length}-dni,"\
        "do-{max_price}zl,{transportation},{amenities},{stars},{departure_city},"\
        "za-wszystkich".format(country=self.country,iteration=self.iteration,date_from=self.date_from,date_to=self.date_to,stay_length=self.stay_length,
        max_price=self.max_price, transportation=self.transportation, amenities=self.amenities, stars=self.stars, 
        departure_city=self.departure_city)

    def add_next_page_num_to_url(self):
        self.iteration += 1
        self.format_url()