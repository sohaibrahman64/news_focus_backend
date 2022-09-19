from flask import Blueprint, request, jsonify
from newspaper import Article
from sqlalchemy import desc

from app import db
# import config
from app.all_news.models import AllNews, AllNewsSchema
from gnews import GNews

# Init Schema
from app.categories.controllers import get_category_name
from app.constants import URL_PREFIX, NEWS_CATEGORIES

all_news_schema = AllNewsSchema()
all_news_schemas = AllNewsSchema(many=True)

# Define the blueprint: 'all_news', its url prefix: app.url/all_news
mod_all_news = Blueprint('all_news', __name__, url_prefix=URL_PREFIX)


def insert_all_news(database):
    gnews = GNews()
    for i in range(len(NEWS_CATEGORIES)):
        cat_id = NEWS_CATEGORIES[i]['id']
        cat_name = NEWS_CATEGORIES[i]['name']
        news = gnews.get_news(cat_name)
        for j in range(len(news)):
            title = news[j]['title']
            description = news[j]['description']
            pub_date = convert_to_datetime(news[j]['published date'])
            url = news[j]['url']
            publisher_name = news[j]['publisher']['title']
            publisher_url = news[j]['publisher']['href']
            image = get_article_image(gnews, url)
            # image = 'empty'
            all_news_ = AllNews.query.filter_by(title=title).first()
            if not all_news_:
                all_news_ = AllNews(cat_id, title, description, pub_date, url, publisher_name, publisher_url, image)
                session = database.session()
                session.add(all_news_)
                session.commit()
                session.close()


# To commit
def convert_to_datetime(date_time_str):
    from datetime import datetime
    date_time_obj = datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S GMT')
    return date_time_obj


# Commit 3
def format_datetime(date_time):
    from datetime import datetime
    date_time_obj = datetime.strftime(date_time, '%d %b')
    return date_time_obj


@mod_all_news.route('/all_news/<cat_id>', methods=['GET', 'PUT'])
def query_all_news(cat_id):
    news = AllNews.query.filter_by(cat_id=cat_id).order_by(desc(AllNews.pub_date)).all()  # Commit 2
    news_list = []
    for single_news in news:
        news_map = {
            'id': single_news.id,
            'cat_id': single_news.cat_id,
            'title': single_news.title,
            'description': single_news.description,
            'pub_date': format_datetime(single_news.pub_date),
            'url': single_news.url,
            'publisher_name': single_news.publisher_name,
            'publisher_url': single_news.publisher_url,
            'image': single_news.image
        }
        news_list.append(news_map)
    return jsonify({'status': '1', 'message': 'Success', 'data': news_list}), 200


def delete_all_news(database):
    database.session.query(AllNews).delete()
    database.session.commit()


# Commit 1
def get_article_image(gnews, url):
    article = gnews.get_full_article(url)
    if article is not None:
        return article.top_image
    else:
        return 'NA'
