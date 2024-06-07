from app import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask import flash
from datetime import date, datetime


@login_manager.user_loader
def load_user(id_usuario):
    return tb_usuario.query.get(id_usuario)


class tb_usuario(database.Model, UserMixin):
    __tablename__ = "tb_usuario"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    sobre_nome = database.Column(
        database.String(50), nullable=False
    )  # Agrega una longitud máxima
    email = database.Column(
        database.String(120), nullable=False, unique=True
    )  # Agrega una longitud máxima
    cpf = database.Column(
        database.String(11), nullable=False
    )  # Asume longitud estándar para CPF
    data_nascimento = database.Column(database.Date, nullable=False)
    telefone = database.Column(
        database.String(20), nullable=False
    )  # Asume una longitud razonable
    senha = database.Column(
        database.String(128), nullable=False
    )  # Asegura una longitud suficiente para contraseñas cifradas
    foto_perfil = database.Column(
        database.String(120), default="Default.jpg"
    )  # Agrega una longitud máxima
    data_criado = database.Column(
        database.DateTime, nullable=False, default=datetime.now
    )
    data_modificado = database.Column(
        database.DateTime, nullable=False, default=datetime.now
    )

    def Login(email, senha):

        try:

            usuario = tb_usuario.query.filter_by(email=email, senha=senha).first()

            if usuario:
                return usuario
            else:
                return None
        except Exception as e:
            flash("Ocorreu um erro durante o login: {}".format(str(e)))
            return None

    def CadastroUsuario(nome, sobre_nome, email, cpf, data_nascimento, telefone, senha):
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        try:
            query = tb_usuario(
                nome=nome,
                sobre_nome=sobre_nome,
                email=email,
                cpf=cpf,
                data_nascimento=data_nascimento,
                telefone=telefone,
                senha=senha
            )

            database.session.add(query)
            database.session.commit()

            print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS", query)
        
            return query
        except Exception as e:

            database.session.rollback()
            flash("Ocorreu um erro durante o cadastro: {}".format(str(e)))
            return e
