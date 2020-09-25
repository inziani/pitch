import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Pitch, Comment

class UserModelTest(unittest.TestCase):
  def test_password_setter(self):
    u1 = User(password = 'test')
    self.assertTrue(pw.password_hash is not None)

  def test_no_password_getter(self):
    u1 = User(password = 'test')
    with self.assertRaises(AttributeError):
      pw.password

  def test_password_verification(self):
    u1 = User(password = 'test')
    self.assertTrue(pw.verify_password('test'))
    self.assertFalse(pw.verify_password('nottest'))

  def test_password_hashed_randomly(self):
    u1 = User(password = 'test')
    u2 = User(password = 'testy')
    self.assertTrue(u1.password_hash != u2.password_hash)




