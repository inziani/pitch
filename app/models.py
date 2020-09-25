from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))




class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique=True, nullable=False, index=True)
  email = db.Column(db.String(125), unique=True, nullable=False, index=True)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password_hash = db.Column(db.String(128), nullable=False)
  pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
  
  

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self):
    self.password_hash = generate_password_hash(password)

  def verify_password(self):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(125), nullable=False)
  category = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  


  def __repr__(self):
    return f"User('{self.title}', {self.category}, '{self.date_posted}')"

  
class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.String(255), nullable=False)
  timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  disabled = db.Column(db.Boolean)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
 
 


  def __repr__(self):
    return f"User('{self.user_id}', '{self.comment}', {self.timestamp})"