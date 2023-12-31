"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
    db.app = app
    with app.app_context():
        db.init_app(app)
    
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    posts = db.relationship("POST", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"
class POST(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    title = db.Column(db.Text,
                nullable=False,
                unique=True)
    content = db.Column(db.Text,
                nullable=False,
                unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

@property
def friendly_date(self):

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")


def connect_db(app):

    db.app = app
    db.init_app(app)
    
class PostTag(db.Model):
    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer,
            db.ForeignKey('posts.id'),
            primary_key=True,
            autoincrement=True)
    tag_id = db.Column(db.Integer,
            db.ForeignKey('tags.id'),
            primary_key=True,
            nullable=False)
    
class Tag(db.Model):
    __tablename__='tags'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text, 
                   nullable=False,
                   unique=True)
    posts=db.relationship(
        'POST',
        secondary="post_tags",
        backref="tags"
    )

