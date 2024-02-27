from app.extensions import db

class Search_param(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(60),nullable=False)
    date_from = db.Column(db.DateTime(60),nullable=False)
    date_to = db.Column(db.DateTime(60),nullable=False)
    stay_length = db.Column(db.String(60),nullable=False)
    stars = db.Column(db.String(60),nullable=False)
    max_price = db.Column(db.String,nullable=False)
    transportation = db.Column(db.String(60),nullable=False)
    amenities = db.Column(db.String(60),nullable=False)
    departure_city = db.Column(db.String(60),nullable=False)
    rating = db.Column(db.String(60),nullable=False)