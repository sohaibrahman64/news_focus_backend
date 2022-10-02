from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from .config import Config

# Define the WSGI application object
# from app.categories.models import Categories
from app.constants import NEWS_CATEGORIES

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Init Marshmallow
ma = Marshmallow(app)

# Import module / component using its blueprint handler variable
from app.categories.controllers import mod_categories as categories_module, insert_categories
from app.categories.controllers import categories_schemas
from app.all_news.controllers import mod_all_news as all_news_module, insert_all_news, query_all_news_articles, \
    delete_all_news
from app.full_article.controllers import mod_full_article as full_article_module
from app.full_article.controllers import insert_full_articles, delete_full_articles

app.register_blueprint(categories_module)
app.register_blueprint(all_news_module)
app.register_blueprint(full_article_module)

# Build the database
# This will create the database file using SQLAlchemy
db.create_all()
#
insert_categories(db)
delete_all_news(db)
insert_all_news(db)

all_news_articles = query_all_news_articles()
delete_full_articles(db)
insert_full_articles(db, all_news_articles)

# from app.cron import init_scheduler

# init_scheduler(db)
