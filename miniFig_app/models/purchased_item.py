from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Purchased_item(db.Model):
    __tablename__ = "purchased_items"

    id = db.Column(db.Integer, primary_key=True)
    sell_fig_id = db.Column(db.Integer, db.ForeignKey('sell_figs.id'))
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'))


    def __repr__(self):
        return '<Purchased_item {}>'.format(self.__dict__)