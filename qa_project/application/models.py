from application import db


# class Customers(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     firstName = db.Column(db.String(50), nullable = False)
#     lastName = db.Column(db.String(50), nullable = False)
#     email = db.Column(db.String(30), unique = True, nullable = False)
#     Address = db.Column(db.String(60), nullable = False)
#     phoneNumber = db.Column(db.Integer, nullable = False)
#     postalCode = db.Column(db.String(7), nullable= False)





# class Products(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     Name = db.Column(db.String(60), unique = True)
#     Description = db.Column(db.String(100), nullable = False)
#     Delivery = db.Relationship('Delivery', backref='products')
    

# class Delivery(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     orders_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))
#     products_id = db.Column('products_id', db.Integer, db.ForeignKey('products.id'))