from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Mensagem personalizada da Juliana"