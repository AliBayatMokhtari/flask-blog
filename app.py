from flask import Flask
from middlewares.auth_middleware import token_required
from auth.auth import auth_blueprint
from db.db import DatabaseConnection

app = Flask(__name__)

if __name__ == '__main__':

  from config import SECRET_KEY, URL_PREFIX

  app.config["SECRET_KEY"] = SECRET_KEY

  app.register_blueprint(auth_blueprint, url_prefix=URL_PREFIX)

  db_connection = DatabaseConnection()

  db_connection.open_connection()

  app.run(host='localhost', port=8080, debug=True)
