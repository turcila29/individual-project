# individual-project

CREATE TABLE customers(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(30) NOT NULL,
    address VARCHAR(80) NOT NULL,
    phoneNum INT NOT NULL,
    postalCode VARCHAR(7) NOT NULL);

CREATE TABLE purchase(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    customer_ID INT,
    purchaseDate DATE,
    totalPrice INT,
    FOREIGN KEY(customer_ID) REFERENCES customers(ID));

CREATE TABLE purchase_item(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    stock_ID INT,
    purchase_ID INT,
    FOREIGN KEY(stock_ID) REFERENCES stock(ID),
    FOREIGN KEY(purchase_ID) REFERENCES purchase(ID));

CREATE TABLE stock(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    description VARCHAR(500) NOT NULL,
    category VARCHAR(30) NOT NULL,
    price INT NOT NULL);


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")



    # @app.route('/cart')
# def cart():
#     all_orders = Order_detail.query.all()
#     order_string = 0
#     for order in all_orders:
#         order_string += order.quantity * order.price
#     return "total: " + str(round(order_string, 2))




# @app.route('/cart')
# def cart():
#     all_orders = Order_detail.query.all()
#     total_amount = 0
#     for order in all_orders:
#         total_amount += order.price
#     return render_template('prodcut2.html', all_orders=all_orders, total_amount=total_amount)

{{ form.hidden_tag() }}

{% if product.id == order.product_id %} 
{% endif %}