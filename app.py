from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Base de datos simulada
usuarios = []

# Página principal
@app.route("/")
def index():
    return render_template("index.html", usuarios=usuarios, resultado_busqueda=None)

# Agregar usuario
@app.route("/agregar", methods=["POST"])
def agregar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]

    usuarios.append({
        "id": id,
        "nombre": nombre,
        "correo": correo
    })

    return redirect(url_for("index"))

# Eliminar usuario
@app.route("/eliminar/<id>")
def eliminar(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return redirect(url_for("index"))

# Editar usuario
@app.route("/editar/<id>")
def editar(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    return render_template("index.html", usuarios=usuarios, editar_usuario=usuario, resultado_busqueda=None)

# Actualizar usuario
@app.route("/actualizar/<id>", methods=["POST"])
def actualizar(id):
    for u in usuarios:
        if u["id"] == id:
            u["nombre"] = request.form["nombre"]
            u["correo"] = request.form["correo"]
    return redirect(url_for("index"))

# BUSCAR usuario por ID
@app.route("/buscar", methods=["POST"])
def buscar():
    id_buscar = request.form["id_buscar"]

    resultado = next((u for u in usuarios if u["id"] == id_buscar), None)

    return render_template(
        "index.html",
        usuarios=usuarios,
        resultado_busqueda=resultado,
        editar_usuario=None
    )

if __name__ == "__main__":
    app.run(debug=True)
