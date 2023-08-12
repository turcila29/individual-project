from application import app, db
# from application import Customer
from flask import render_template


@app.route("/")
def home():
    return render_template('layout.html')

# @app.route("/")
    