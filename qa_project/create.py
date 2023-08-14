from application import db, app
from application.models import customers, purchase, purchase_item, stock

with app.app_context():
    db.drop_all()
    db.create_all()

