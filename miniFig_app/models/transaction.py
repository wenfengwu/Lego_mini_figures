from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db
from sqlalchemy.orm import relationship

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    purchased_item = relationship("Purchased_item")

    def __repr__(self):
        return '<Transaction {}>'.format(self.__dict__)