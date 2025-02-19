# app/controllers/user_controller.py

from app.models import User
from app import db


def add_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
