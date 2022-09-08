from flask import Blueprint, request, jsonify
from app import db
import config
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
            all_news_ = AllNews.query.filter_by(title=title).first()
            if not all_news_:
                all_news_ = AllNews(cat_id, title, description, pub_date, url, publisher_name, publisher_url)
                session = database.session()
                session.add(all_news_)
                session.commit()
                session.close()


def convert_to_datetime(date_time_str):
    from datetime import datetime
    date_time_obj = datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S GMT')
    return date_time_obj


@mod_all_news.route('/all_news/<cat_id>', methods=['GET', 'PUT'])
def query_all_news(cat_id):
    news = AllNews.query.filter_by(cat_id=cat_id).all()
    news_list = []
    for single_news in news:
        news_map = {
            'id': single_news.id,
            'cat_id': single_news.cat_id,
            'title': single_news.title,
            'description': single_news.description,
            'pub_date': single_news.pub_date,
            'url': single_news.url,
            'publisher_name': single_news.publisher_name,
            'publisher_url': single_news.publisher_url
        }
        news_list.append(news_map)
    return jsonify({'status': '1', 'message': 'Success', 'data': news_list}), 200


def delete_all_news(database):
    database.session.query(AllNews).delete()
    database.session.commit()
