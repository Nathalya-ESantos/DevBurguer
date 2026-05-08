from flask import Flask, render_template, redirect, request, session, jsonify
from model.produto import recuperar
from model.produto import rec_destaq
from model.produto import rec_produto
from model.usuario import Usuario
from model.carrinho import recuperar_carrinho
from model.carrinho import inserir_item


app = Flask(__name__)

app.secret_key = "chiclete"

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

    if  resultado:
        session["usuario_logado"] = resultado
        return redirect("/")
    else:
        return "Usuario Incorreto"

    

@app.route("/api/get/carrinho", methods=["GET"])
def api_get_carrinho():
    usuario_logado = session.get("usuario_logado")

    
    # jsonify: Traduz os dados do Python/Banco para o formato JSON (texto universal).
    # O Front-end recebe este JSON e consegue desenhar os itens na tela.
    # 200 = Sucesso | 401 = Não autorizado (Erro de Login).
    if "usuario_logado" in session:
        usuario =session["usuario_logado"]["USUARIO"]
        carrinho = recuperar_carrinho(usuario)
        return jsonify(carrinho), 200
    else:
        return jsonify({"message": "Usuario não logado"}), 401
    

@app.route("/api/post/carrinho", methods=["POST"])
def api_post_carrinho():

   if "usuario_logado" in session:
       usuario = session["usuario_logado"] ["USUARIO"]
       dados_json = request.get_json()
       codigo_produto = dados_json.get("cod_produto")
       quantidade = dados_json.get("quantidade")

       inserir_item (usuario, codigo_produto, quantidade)
       return jsonify({"message":"Inserido com sucesso"}), 201
   else:
       return redirect ("/login")

@app.route("/cadastro_login")
def cadastro_login():
    return render_template("cadastro_login.html")



app.run(debug=True)