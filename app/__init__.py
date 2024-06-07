from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "3364a1b3b9c120a257319a7b7c503903"
app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc://sa:Root1234@DOUG\SQLEXPRESS/PROJETOS?driver=ODBC+Driver+17+for+SQL+Server'



database = SQLAlchemy(app)
migrate = Migrate(app,database)
login_manager = LoginManager(app)

from app import routes