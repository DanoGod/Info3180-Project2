from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = "aeiou"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://finalproject:LabLab@localhost:5432/finalproject"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
