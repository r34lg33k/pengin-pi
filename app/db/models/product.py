from app.db import db
from app.util.uuid import id


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(36), default=id, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    price = db.Column(db.String(100))
    article = db.Column(db.String(10000))
    card_image_url = db.Column(db.String(500))
    stock_image_url = db.Column(db.String(500))
