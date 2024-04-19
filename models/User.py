from app import db

db_core = db.get_core()

class User(db_core.Model):
  id = db_core.Column(db_core.Integer, primary_key=True)
  name = db_core.Column(db_core.String(20))
