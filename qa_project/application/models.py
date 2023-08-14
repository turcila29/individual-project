from application import db
from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class


class customers(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    Address = db.Column(db.String(60), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    postalCode = db.Column(db.String(7), nullable=False)
    products = db.relationship('purchase', backref='customers')

class purchase(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    customer_ID = db.Column(db.Integer, db.ForeignKey('customers.ID'), nullable=False)
    purchaseDate = db.Column(db.DateTime, nullable=False)
    totalPrice = db.Column(db.Integer, nullable=False)
    item = db.relationship('purchase_item', backref='purchase')
    
class purchase_item(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    purchase_ID = db.Column(db.Integer, db.ForeignKey('purchase.ID'), nullable=False)
    stock_ID = db.Column(db.Integer, db.ForeignKey('stock.ID'), nullable=False)

class stock(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    item = db.relationship('purchase_item', backref='stock')

