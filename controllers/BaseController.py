from db import Database

class BaseController:
  def __init__(self, db: Database) -> None:
    self.session = db.get_session()
