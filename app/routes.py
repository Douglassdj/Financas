from app import app
from flask import render_template, request, url_for, redirect
from flask_login import login_user

from app.Models.model_usuario import tb_usuario


@app.route("/")
def LoginGet():
    return render_template("login/login.html")


@app.route("/login", methods=["POST"])
def LoginPost():

    if request.method == "POST":
        email = request.form.get("email", default="")
        senha = request.form.get("senha", default="")
        
        login = tb_usuario.Login(email, senha)

        if login:
            login_user(login)
            return redirect(url_for("HomeGet"))
        else:
            message = {
                "icon": "error",
                "title": "Tentativa de login falhou",
                "text": "Usuário ou senha inválidos.",
            }

    return render_template("login/login.html", message=message)

@app.route("/cadastro-usuario")
def CastroUsuarioGet():

    return render_template(
        "login/cadastro_usuario.html"
    )
    
    
@app.route("/cadastro-usuario/Confirmar", methods=['POST'])
def CastroUsuarioPost():
    nome = request.form.get('nome',default='')
    sobre_nome = request.form.get('sobre_nome',default='')
    email = request.form.get('email',default='')
    telefone = request.form.get('telefone',default='')
    cpf = request.form.get('cpf',default='')
    data_nascimento = request.form.get('data_nascimento',default='')
    senha = request.form.get('senha',default='')
    confirma_senha = request.form.get('confirma_senha',default='')
    
    
    cadastro = tb_usuario.CadastroUsuario(nome,sobre_nome,email,cpf,data_nascimento,telefone,senha)

    if cadastro:
        message ={
            "icon": "success",
            "title": "Cadastro concluido",
            "text": "Cadastro conncluido com sucesso. Faca login"   
        }
        return render_template("login/cadastro_usuario.html", message=message)
    else:        
        message ={
            "icon": "error",
            "title": "Erro ao tentar cadastrar",
            "text": f"{cadastro}"   
        }
        return render_template("login/cadastro_usuario.html", message=message)


@app.route("/home")
def HomeGet():
    return render_template("plataforma/home.html")

@app.route("/contas")
def ContasGet():
    return render_template("plataforma/contas.html")

@app.route("/transacoes")
def TransacoesGet():
    return render_template("plataforma/transacoes.html")

@app.route("/cartao-credito")
def CartaoCreditoGet():
    return render_template("plataforma/cartao_credito.html")

@app.route("/planejamento")
def PlanejamentoGet():
    return render_template("plataforma/planejamento.html")

@app.route("/objetivos")
def ObjetivosGet():
    return render_template("plataforma/objetivos.html")

@app.route("/categorias")
def CategoriasGet():
    return render_template("plataforma/categorias.html")

@app.route("/perfil")
def PerfilGet():
    return render_template("plataforma/perfil_usuario.html")
