from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from miniFig_app import db


class Figure(db.Model):
    __tablename__ = "figures"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    theme = db.Column(db.String(255))
    img_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    sell_fig = relationship("Sell_fig")

    def __repr__(self):
        return '<Figure {}>'.format(self.__dict__)

    @classmethod
    def browse_all(cls, offset=0, page_size=100):
        browse_figs = Figure.query.limit(page_size).offset(offset).all()  # select *
        return browse_figs

    @classmethod
    def count_all(cls):
        count_figs = Figure.query.count()
        return count_figs
    # session_browse.close()

    @classmethod
    def browse_all_by_year(cls,year,offset=0, page_size=100):
        browse_figs = Figure.query.filter(Figure.year == year).limit(page_size).offset(offset).all()
        return browse_figs

    @classmethod
    def browse_all_by_theme(cls, theme,offset=0, page_size=100):
        browse_figs = Figure.query.filter(Figure.theme == theme).limit(page_size).offset(offset).all() # select * by theme
        return browse_figs

    @classmethod
    def get_one_by_fig_id(cls, id):
        return Figure.query.filter(Figure.id == id).one()

    # search bar select by search term
    @classmethod
    def search_by_name(cls, term, limit=6):
        return Figure.query.filter(Figure.name.contains(term)).limit(limit).all()
