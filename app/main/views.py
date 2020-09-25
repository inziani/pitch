from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_user, login_required
from . import main
from .. import db
from ..models import User, Pitch, Comment

@main.route('/')
@login_required
def home():
  return render_template('home.html')