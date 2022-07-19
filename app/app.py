import datetime
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .functions.reader import reader
from .functions.converter import convert

# Configurations
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Used model
class Product(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    number_of_order = db.Column(db.String(30), nullable=False, unique=True)
    time = db.Column(db.Date, nullable=False)
    price_usd = db.Column(db.Integer, nullable=False)
    price_rub = db.Column(db.Integer, nullable=False)


def __repr__(self):
    return self.order


@app.route('/', methods=['GET', 'POST'])
def main():
    res = reader()
    for i in res:
        if not Product.query.filter_by(number_of_order=i[1]).first():
            product = Product(
                number=i[0],
                number_of_order=i[1],
                price_usd=i[2],
                price_rub=convert(int(i[3][:2]), i[3][3:5], int(i[3][6:10]), i[2]),
                time=datetime.date(int(i[3][6:10]), int(i[3][3:5]), int(i[3][:2]))
            )
            try:
                db.session.add(product)
                db.session.commit()
            except ImportError:
                return 'Ops, something is going wrong'
    db_products = Product.query.all()
    return render_template('index.html', db_products=db_products)
