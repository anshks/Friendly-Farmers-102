from flask import (
    Flask,
)
from flask_bootstrap import Bootstrap
import os, random
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
Bootstrap(app)
from app.query_helper import ( init_db )
app.config['SECRET_KEY'] = "SECRET"
app.config['DATABASE_PATH'] = "app.db"
app.config['PER_PAGE'] = 10
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(__name__)
print('\n\n\n> Running init db', random.random(), '\n')
init_db()
from app import routes