from db.db import Database
from models import User
from .BaseController import BaseController

class UserController(BaseController):
  def __init__(self, db: Database) -> None:
    super().__init__(db)

  def create_user(self):
    # NOTE: user should be of type dto as parameter
    user = User(name="Ali", fullname="Bayat Mokhtari")
    self.session.add(user)
    self.session.commit()
