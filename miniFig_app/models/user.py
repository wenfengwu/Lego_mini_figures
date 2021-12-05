from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db
from sqlalchemy.orm import relationship
from miniFig_app import login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(60)) 
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    cart = relationship("Cart")
    sell_fig = relationship("Sell_fig")
    transaction = relationship("Transaction")

    def __repr__(self):
        return '<User {}>'.format(self.__dict__)
        
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def set_password(self, password):
        self.password = password

    @classmethod
    def update_info(cls, form, user_id):
        User.query.filter(User.id==int(user_id)).update(
            dict(username=form.username.data, email=form.email.data)
        )
        db.session.commit()
