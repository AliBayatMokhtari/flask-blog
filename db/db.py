from helpers import SingletonMeta
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DATABASE_URI_KEY

class Database(metaclass=SingletonMeta):
  def __init__(self, app: Flask, connection_string: str):
    super()
    app.config[DATABASE_URI_KEY] = connection_string
    self.core = SQLAlchemy(app)

  def get_core(self):
    return self.core
  
  def get_session(self):
    return self.core.session
  
  def create_all(self):
    self.core.create_all()
    print("Successfully created database...")
