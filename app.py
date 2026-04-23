from flask import Flask, render_template, redirect, request, session
from model.produto import recuperar
from model.produto import rec_destaq
from model.produto import rec_produto
from model.usuario import Usuario


app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar()
    destaques = rec_destaq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<codigo>")
def pagina_produto(codigo):
    produto = rec_produto(codigo)
   
    return render_template("produto.html", produto = produto)

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

@app.route("/logar/usuario", methods=["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuario.logar(usuario, senha)

    if not resultado:
        session["usuario_logado"] = resultado

    return redirect("/")

@app.route("/cadastro_login")
def cadastro_login():
    return render_template("cadastro_login.html")

app.run(debug=True)