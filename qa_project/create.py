from application import db, app
from application.models import Customer, Order, Product, Order_detail
from application import routes


with app.app_context():
    db.drop_all()
    db.create_all()

    chanel = Product(name="Platinum Egoiste Chanel", description="A thrilling scent for summer", price=100, stock_quantity=100)
    db.session.add(chanel)
    db.session.commit()

    armani = Product(name="Acqua di Gio Armani", description="Best man fragrance", price=120, stock_quantity=100)
    db.session.add(armani)
    db.session.commit()

    givenchy = Product(name="L'interdit Givenchy", description="A fine gourmont scent", price=150, stock_quantity=100)
    db.session.add(givenchy)
    db.session.commit()

    moschino = Product(name="Toyboy Moschino", description="Best spicy fragrance", price=112, stock_quantity=100)
    db.session.add(moschino)
    db.session.commit()

    testuser = Order_detail(order_id=1, product=chanel, quantity=10)
    testuser.price = chanel.price 
    db.session.add(testuser)
    db.session.commit()

    testapple = Order_detail(order_id=2, product=armani, quantity=5)
    testapple.price = armani.price 
    db.session.add(testapple)
    db.session.commit()

    testuser = Order_detail(order_id=3, product=givenchy, quantity=6)
    testuser.price = givenchy.price
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=4, product=moschino, quantity=10)
    testuser.price = moschino.price
    db.session.add(testuser)
    db.session.commit()
    

