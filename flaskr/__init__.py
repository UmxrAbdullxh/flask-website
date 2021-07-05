from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b67787eafd1e03c99d2f1f77'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login_form'
login_manager.login_message_category = "info"
from flaskr import routes
