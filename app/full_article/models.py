from app import db, ma


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class FullArticle(Base):
    news_id = db.Column(db.Integer, db.ForeignKey('all_news.id'))
    cat_id = db.Column(db.Integer, db.ForeignKey('all_news.cat_id'))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    text = db.Column(db.Text(2048))
    image = db.Column(db.String(100))
    publisher_name = db.Column(db.String(100))
    pub_date = db.Column(db.DateTime())
    keywords = db.Column(db.String(100))

    def __init__(self, news_id, cat_id, title, author, text, image, publisher_name, pub_date, keywords):
        self.news_id = news_id
        self.cat_id = cat_id
        self.title = title
        self.author = author
        self.text = text
        self.image = image
        self.publisher_name = publisher_name
        self.pub_date = pub_date
        self.keywords = keywords

    def __repr__(self):
        return '<FullArticle: %s>' % self.title


class FullArticleSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'news_id', 'cat_id', 'title', 'author', 'text', 'image', 'publisher_name', 'pub_date', 'keywords')
