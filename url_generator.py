class Url_generator:


    def __init__(self, **kwarg):
        self.country = kwarg['country']
        self.date_from = kwarg['date_from']
        self.date_to = kwarg['date_to']
        self.stay_length = kwarg['stay_length']
        self.max_price = kwarg['max_price']
        self.transportation = kwarg['transportation']
        self.amenities = kwarg['amenities']
        self.stars = kwarg['stars']
        self.depature_city = kwarg['depature_city']


    def format_url(self):
        url = "https://www.wakacje.pl/wczasy/{country}/?od-{date_from},do-{date_to},{stay_length}-dni,\
        do-{max_price}zl,{transportation},{amenities},{stars},{depature_city},\
        za-wszystkich&src=fromFilters".format(country=self.country,date_from=self.date_from,date_to=self.date_to,stay_length=self.stay_length,
        max_price=self.max_price, transportation=self.transportation, amenities=self.amenities, stars=self.stars, 
        depature_city=self.depature_city)
        return url