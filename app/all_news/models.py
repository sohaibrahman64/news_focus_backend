from app import db, ma

# Define a base model for other database table to inherit
from app.full_article.models import FullArticle


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class AllNews(Base):
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    pub_date = db.Column(db.DateTime())
    url = db.Column(db.String(100))
    publisher_name = db.Column(db.String(100))
    publisher_url = db.Column(db.String(100))
    image = db.Column(db.String(100))
    # full_article = db.relationship("FullArticle", backref="full_article", lazy=True,
    #                                primaryjoin=(FullArticle.news_id == id))

    def __init__(self, cat_id, title, desc, pub_date, url, pub_name, pub_url, image):
        self.cat_id = cat_id
        self.title = title
        self.description = desc
        self.pub_date = pub_date
        self.url = url
        self.publisher_name = pub_name
        self.publisher_url = pub_url
        self.image = image

    def __repr__(self):
        return '<AllNews: %s>' % self.title


class AllNewsSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'cat_id', 'title', 'description', 'published_date', 'url', 'publisher_name', 'publisher_url', 'image')
