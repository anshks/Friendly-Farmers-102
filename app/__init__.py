from flask import (
    Flask,
)
from flask_bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "SECRET"
app.config['DATABASE_PATH'] = "app.db"
app.config['PER_PAGE'] = 10
app.config.from_object(__name__)

from app import routes
