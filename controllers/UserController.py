from db.db import Database
from models import User
from .BaseController import BaseController
from schemas import users_schema, user_schema

class UserController(BaseController):
  from app import db

  def __init__(self, db: Database = db) -> None:
    super().__init__(db)

  def create_user(self, user):
    data = user_schema.load(user)
    new_user = User(name=data["name"])
    self.session.add(new_user)
    self.session.commit()
    return user

  def users_list(self):
    users = User.query.all()
    result = users_schema.dump(users)
    return result
