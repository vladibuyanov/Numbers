from datetime import date
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from reader import full
from convert_to_usd import convert

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    number_of_order = db.Column(db.String(30), nullable=False, unique=True)
    time = db.Column(db.DateTime, nullable=False)
    price_usd = db.Column(db.Integer, nullable=False)
    price_rub = db.Column(db.Integer, nullable=False)


def __repr__(self):
    return self.order


@app.route('/', methods=['GET', 'POST'])
def main():
    db_products = Product.query.all()
    for i in full:
        if not Product.query.filter_by(number_of_order=i[1]).first():
            product = Product(
                number=i[0],
                number_of_order=i[1],
                price_usd=i[2],
                price_rub=convert('28/04/2022', i[2]),
                time=date(full[i][3][6:10], full[i][3][3:5], full[i][3][:2])
            )
            try:
                db.session.add(product)
                db.session.commit()
            except ImportError:
                return 'Ops, something is going wrong'
    return render_template('index.html', db_products=db_products)


if __name__ == '__main__':
    app.run()
