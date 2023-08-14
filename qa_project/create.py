from application import db, app
from application.models import Customer, Order, Product, Order_detail
from application import routes


with app.app_context():
    db.drop_all()
    db.create_all()

    testuser = Order_detail(order_id=1, product_id=1, quantity=10, price=12.50)
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=2, product_id=2, quantity=5, price=20.45)
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=3, product_id=3, quantity=6, price=60.65)
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=4, product_id=4, quantity=3, price=90.23)
    db.session.add(testuser)
    db.session.commit()