from db.db import Database
from .BaseController import BaseController

class AuthController(BaseController):
  from app import db

  def __init__(self, db: Database = db) -> None:
    super().__init__(db)

  def login(self):
    pass

  def logout(self):
    pass
