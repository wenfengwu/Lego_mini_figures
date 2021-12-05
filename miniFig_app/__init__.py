from flask import Flask
from miniFig_app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy()
db.init_app(app)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

# Create migration script
migrate = Migrate(app, db)

from miniFig_app.models.figure import Figure # import model class so it can be initalized
from miniFig_app.models.user import User # import model class so it can be initalized
from miniFig_app.models.cart import Cart # import model class so it can be initalized
from miniFig_app.models.purchased_item import Purchased_item # import model class so it can be initalized
from miniFig_app.models.transaction import Transaction # import model class so it can be initalized
from miniFig_app.models.sell_fig import Sell_fig # import model class so it can be initalized


# Create database table
with app.app_context():
    engine = db.get_engine()
    with engine.connect() as conn:
        conn.execute(f"CREATE DATABASE IF NOT EXISTS minifigs")
    db.create_all()

from miniFig_app.routes import index_route # import index_route
from miniFig_app.routes import user_route # import user_route
from miniFig_app.routes import browse_route # import user_route
from miniFig_app.routes import sell_fig_route # import sell_fig_route
from miniFig_app.routes import cart_route # import cart_route
