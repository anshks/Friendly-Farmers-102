import os, random
from flask import ( Flask, )
from flask_bootstrap import Bootstrap
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
Bootstrap(app)
from app.query_helper import ( init_db )
app.config['SECRET_KEY'] = "SECRET"
app.config['DATABASE_PATH'] = "app.db"
app.config['PER_PAGE'] = 10
#Reload whenever templates changes are detected: 
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(__name__)
#Setting up the initial database: 
print('\n\n\n> Running init db\n')
init_db()
from app import routes