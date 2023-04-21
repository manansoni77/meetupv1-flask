import os
from flask import Flask
from app.models import db
from config import *

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = app.config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, DB_NAME)

db.init_app(app)

if not os.path.exists(os.path.join(current_dir, DB_NAME)):
    print(db.create_all(app=app))

app.app_context().push()

from app.routes import *

if __name__ == '__main__':
    app.run(debug=True, port=8080)