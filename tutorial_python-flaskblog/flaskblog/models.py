from datetime import datetime
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # how SQLAlchemy deals with relationships (in this case, 1-M)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        # how the object is printed whenever we print it out
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # utcnow is a function. Want to pass in the function itself, so don't add the parantheses 
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # how the object is printed whenever we print it out
        return f"User('{self.title}', '{self.date_posted}')"