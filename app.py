from flask import Flask, render_template
from model.produto import recuperar


app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar()
    return render_template("index.html", produtos = produtos)

@app.route("/produto")
def pagina_produto():
    
    return render_template("produto.html")

app.run(debug=True)