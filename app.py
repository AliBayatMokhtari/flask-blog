from flask import Flask
from auth import auth_blueprint
from db import Database

app = Flask(__name__)

if __name__ == '__main__':
  from config import SECRET_KEY, URL_PREFIX

  app.config["SECRET_KEY"] = SECRET_KEY
  app.register_blueprint(auth_blueprint, url_prefix=URL_PREFIX)

  db_name = "db"
  connection_string = f"sqlite:///{db_name}.sqlite"
  db = Database(connection_string)
  db.open_connection()
  db.create_all()

  app.run(host='localhost', port=8080, debug=True)
