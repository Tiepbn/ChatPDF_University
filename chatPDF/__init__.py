from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
# app.config['SECRET_KEY'] = '8d995ee2e1b43236aaea002c'
# db = SQLAlchemy(app)

# login_manager = LoginManager(app)

from chatPDF import routes