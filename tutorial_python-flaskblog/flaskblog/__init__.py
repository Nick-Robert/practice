from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# three slashes is a relative path from the current file, so the site.db will be created in the same directory as this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # function name of the route, same as the thing you pass in to the url_for() function
login_manager.login_message_category = 'info'

# need to import the routes after the app initialization to avoid circular imports
from flaskblog import routes