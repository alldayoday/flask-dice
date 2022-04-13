#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('DicePost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class DicePost(db.Model):
    __tablename__ = 'dice_posts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    link = db.Column(db.String(140), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, link, user_id):
        self.link = link
        self.user_id = user_id
    
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Link: {self.link}"

class TarotPost(db.Model):
    __tablename__ = 'tarot_posts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    spread = db.Column(db.Text, nullable=False)
    card1 = db.Column(db.Text, nullable=False)
    card2 = db.Column(db.Text, nullable=False)
    card3 = db.Column(db.Text, nullable=False)
    reflection = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, spread, card1, card2, card3, reflection, user_id):
        self.title = title
        self.spread = spread
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.reflection = reflection
        self.user_id = user_id
        
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.Title}"