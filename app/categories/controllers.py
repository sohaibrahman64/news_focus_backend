from flask import Blueprint, request, jsonify
from app import db
import config
from app.categories.models import Categories, CategoriesSchema
from app.constants import NEWS_CATEGORIES, URL_PREFIX

# Init Schema
categories_schema = CategoriesSchema()
categories_schemas = CategoriesSchema(many=True)

# Define the blueprint: 'categories', its url prefix: app.url/categories
mod_categories = Blueprint('categories', __name__, url_prefix=URL_PREFIX)


def insert_categories(database):
    for i in range(len(NEWS_CATEGORIES)):
        cat_id = NEWS_CATEGORIES[i]['id']
        name = NEWS_CATEGORIES[i]['name']
        category = Categories.query.filter_by(name=name).first()
        if not category:
            category = Categories(cat_id, name)
            session = database.session()
            session.add(category)
            session.commit()
            session.close()


def get_category_name(cat_id):
    category = Categories.query.filter_by(id=cat_id).first()
    cat_name = category.name
    return cat_name


# Set the route and accepted methods
@mod_categories.route('/categories', methods=['GET'])
def categories():
    if request.method == 'GET':
        all_categories = Categories.query.all()
        result = categories_schemas.dump(all_categories)
        return jsonify(result), 200
