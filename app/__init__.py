from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = "aeiou"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://drxyxwztwolzpf:f68880fe9c79f93bbf43fb1de7cf7b0d8a644947c0e8ae70ab351011283a7e05@ec2-54-224-120-186.compute-1.amazonaws.com:5432/danpbh5i20o9fn'
HEROKU_POSTGRESQL_AMBER_URL='postgres://tbcmhmpogxxgfw:6913769ad1e0af3491ce12533f120199a244c06317bd81cee15aeb4eba2b4ec4@ec2-3-233-43-103.compute-1.amazonaws.com:5432/ddh5j72ndu04b2'
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
