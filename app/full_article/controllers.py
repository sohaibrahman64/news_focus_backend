from flask import Blueprint, jsonify
from app.full_article.models import FullArticle, FullArticleSchema
from app.constants import URL_PREFIX, NEWS_CATEGORIES
from gnews import GNews
from app.utils.utils import convert_to_datetime, format_datetime

full_article_schema = FullArticleSchema()
full_article_schemas = FullArticleSchema(many=True)

mod_full_article = Blueprint('full_article', __name__, url_prefix=URL_PREFIX)


def parse_keywords(article):
    keys_ = 'NA'
    if len(article.keywords) > 0:
        for j in range(len(article.keywords)):
            keys_ = article.keywords[j]
            if j < len(article.keywords):
                keys_ = keys_.concat(",")
    return keys_


def parse_authors(article):
    authors = 'NA'
    if len(article.authors) > 0:
        authors = ''
        for j in range(len(article.authors)):
            if j < len(article.authors) - 1:
                authors += article.authors[j] + ", "
            else:
                authors += article.authors[j]
    return authors


def insert_full_articles(database, all_news_articles):
    gnews = GNews()
    for i in range(len(all_news_articles)):
        single_article = all_news_articles[i]
        article_url = single_article['url']
        article = gnews.get_full_article(article_url)

        if article is not None:
            news_id = single_article['id']
            cat_id = single_article['cat_id']
            title = single_article['title']
            author = parse_authors(article)
            text = article.text
            image = single_article['image']
            publisher_name = single_article['publisher_name']
            pub_date = article.publish_date
            keywords = parse_keywords(article)

            full_article_ = FullArticle.query.filter_by(title=title).first()
            if not full_article_:
                full_article_ = FullArticle(news_id, cat_id, title, author, text, image, publisher_name, pub_date,
                                            keywords)
                session = database.session()
                session.add(full_article_)
                session.commit()
                session.close()


# Delete all the records
def delete_full_articles(database):
    database.session.query(FullArticle).delete()
    database.session.commit()
