import sqlite3
import os
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
      raise "No open connection found..."
    self.connection.close()
    self.connection = None
    print("Connection closed successfully.")

  def get_connection(self):
    return self.connection
  
  def get_script(script_name: str):
    script_dir = os.path.dirname(__file__)
    rel_path = "queries/" + script_name
    abs_path = os.path.join(script_dir, rel_path)
    return abs_path
  
  def execute_query(self, script_name: str, msg: str):
    script_path = DatabaseConnection.get_script(script_name)
    with open(script_path) as q:
      self.connection.executescript(q.read())
      print(msg)

  def init_database(self):
    if not self.connection:
      self.open_connection()
    script_name = "InitDB.sql"
    msg = "Database initiated successfully."
    self.execute_query(script_name, msg)
