from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista temporal para almacenar tareas en memoria (no se guarda al reiniciar)
tareas = []

@app.route("/", methods=["GET"])
def home():
    return render_template("todo.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    nueva_tarea = request.form["tarea"]
    if nueva_tarea.strip() != "":
        tareas.append(nueva_tarea)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
