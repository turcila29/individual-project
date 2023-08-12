from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from application import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/QA_project'

db = SQLAlchemy(app)

from application import routes