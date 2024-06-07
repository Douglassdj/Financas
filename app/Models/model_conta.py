from app import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask import flash
from datetime import date, datetime



class tb_conta(database.Model, UserMixin):
    __tablename__ = "tb_usuario"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
   
    data_criado = database.Column(database.DateTime, nullable=False, default=datetime.now)
    data_modificado = database.Column(database.DateTime, nullable=False, default=datetime.now)
