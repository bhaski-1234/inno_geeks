from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_cors import CORS, cross_origin
import os


DBUSER = os.getenv('POSTGRES_USER')
DBPASS = os.getenv('POSTGRES_PASSWORD')
DBHOST = os.getenv('POSTGRES_HOST')
DBPORT = os.getenv('POSTGRES_PORT')
DBNAME = os.getenv('POSTGRES_DB')


app = Flask(__name__)
app.secret_key = "foobarbaz"
cors = CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://marco:foobarbaz@database-1.c9dmjrv0kdhi.us-east-2.rds.amazonaws.com:5432/testdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'siddhukanu3@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sidd@2476'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
db=SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes

