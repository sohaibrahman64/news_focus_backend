from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Define the WSGI application object
# from app.categories.models import Categories
from app.constants import NEWS_CATEGORIES

app = Flask(__name__)

# Configurations
app.config.from_object('config.Config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


migrate = Migrate(app, db)

# Init Marshmallow
ma = Marshmallow(app)

# Import module / component using its blueprint handler variable
from app.categories.controllers import mod_categories as categories_module, insert_categories
from app.categories.controllers import categories_schemas
from app.all_news.controllers import mod_all_news as all_news_module, insert_all_news

app.register_blueprint(categories_module)
app.register_blueprint(all_news_module)

# Build the database
# This will create the database file using SQLAlchemy
db.create_all()

insert_categories(db)
insert_all_news(db)

# from app.cron import init_scheduler

# init_scheduler(db)
