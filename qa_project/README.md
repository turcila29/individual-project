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