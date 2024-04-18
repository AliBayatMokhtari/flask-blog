from models import User
from .BaseController import BaseController

class UserController(BaseController):
  def create_user(self):
    # NOTE: user should be of type dto as parameter
    user = User(name="Ali", fullname="Bayat Mokhtari")
    self.session.add(user)
    self.session.commit()
