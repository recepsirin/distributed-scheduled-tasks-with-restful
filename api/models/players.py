from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)


category = ['Beginner', 'Intermediate', 'Advanced', 'Expert', 'Candidate Master', 'Master', 'National Master',
            'Senior Master', 'Grandmaster']


class Player(db.Document):
    rank = db.IntField(required=True, unique=True)
    name = db.StringField(required=True, max_length=50)
    level = db.StringField(required=True, choices=category)
    country = db.StringField(required=True, max_length=50)
    rating = db.IntField(required=True)
