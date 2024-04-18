from helpers import SingletonMeta
import sqlalchemy as sal
from sqlalchemy.orm import Session
from models.Base import Base

class Database(metaclass=SingletonMeta):
  def __init__(self, connection_string: str):
    super()
    self.connection_string = connection_string
    self.engine = None
    self.session = None
    
  def open_connection(self):
    if not self.session:
      self.engine = sal.create_engine(self.connection_string)
      self.session = Session(self.engine)
      print("Successfully connected to database.")

  def close_connection(self):
    if not self.session:
      raise "No open connection found..."
    self.session.close()
    self.session = None
    print("Successfully closed database connection.")

  def get_session(self):
    return self.session

  def create_all(self):
    Base.metadata.create_all(self.engine)
