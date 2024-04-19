from flask import Flask
from flask_migrate import Migrate
from routes import auth_blueprint
from db import Database
from config import SECRET_KEY, URL_PREFIX

# Create Flask application
app = Flask(__name__)

# Set application configurations
app.config["SECRET_KEY"] = SECRET_KEY

# Initiate database instance
db_name = "db"
connection_string = f"sqlite:///{db_name}.sqlite"
db = Database(app, connection_string)
db_core = db.get_core()
migrate = Migrate(app, db_core)

if __name__ == '__main__':
  # Import all models for stupid flask-sqlalchemy to create tables
  import models

  # Set application context and create database
  with app.app_context():
    db.create_all()

  # Register application routes
  app.register_blueprint(auth_blueprint, url_prefix=URL_PREFIX)

  app.run(host='localhost', port=8080, debug=True)
