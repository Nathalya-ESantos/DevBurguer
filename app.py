from flask import Flask, render_template
from model.produto import recuperar
from model.produto import rec_destaq


app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar()
    destaques = rec_destaq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto")
def pagina_produto():

    return render_template("produto.html")

app.run(debug=True)