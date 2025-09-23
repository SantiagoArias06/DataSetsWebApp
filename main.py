# Punto de entrada: corre Flask y rutas principales
from flask import Flask, render_template
from app.controllers import obtener_datos

# Decirle a Flask que las templates están dentro de app/templates
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

@app.route("/")
def index():
    datos = obtener_datos()
    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)
