from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Mensagem personalizada da Juliana para dar erro no pipeline"