from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from flask_login import login_user, login_required, current_user
from .forms import PostForm, CommentForm
from app.models import Pitch, User, Comment
from . import main
from .. import db


@main.route('/')
@main.route('/home')
@login_required
def home():
  page = request.args.get('page', 1, type=int)
  pitches = Pitch.query.order_by(Pitch.category).paginate(page=page, per_page=5)
  comments=Comment.query.order_by(Comment.timestamp.asc())#.paginate(page=page, per_page=5)) # Addition of comments
  return render_template('home.html', pitches=pitches)


@main.route('/pitch/new', methods=['GET', 'POST'] )
@login_required
def new_pitch():
  form = PostForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data, category=form.category.data, content=form.content.data, 
    user_id=current_user.username) 
    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('.home'))
    flash('Your Pitch has been created')
    return redirect(url_for('main.home'))
  return render_template('create.html', form=form, title='new pitch')

  @main.route('/pitch/<int:pitches_id>', methods=['GET', ['POST']])
  @login_required
  def pitch_comment(pitches_id):
    pitch = Pitch.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
      comment = Comment(comment=form.comment.data, pitches_id=pitches_id, user_id=current_user.username)
      db.session.add(comment)
      db.session.commit()
      flash('Your comment has been posted')
      return redirect(url_for('.pitch', pitches_id=pitches.id))
    comments = pitch.comment.query_all()
    return render_template('comments.html', pitch=pitch, form=form, title='Comment')

  
