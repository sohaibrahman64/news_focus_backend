from app import db, ma


# Define a base model for other database table to inherit
class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class Categories(Base):
    name = db.Column(db.String(100))
    all_news = db.relationship("AllNews", backref="all_news", lazy=True)

    def __init__(self, cat_id, name):
        self.id = cat_id
        self.name = name

    def __repr__(self):
        # return '<Category: %s>' % self.name
        return '{id: %s, name: %s}' % (self.id, self.name)


class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
