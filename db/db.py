import sqlite3
from helpers.SingletonMeta import SingletonMeta

class DatabaseConnection(metaclass=SingletonMeta):
  def __init__(self):
    super()
    self.connection = None

  def open_connection(self):
    if not self.connection:
      self.connection = sqlite3.connect("database.db")

  def close_connection(self):
    if not self.connection:
      raise "No Connection found..."
    self.connection.close()
    self.connection = None

  def get_connection(self):
    return self.connection

connection_1 = DatabaseConnection()