from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from models import Alumnos, bd
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modelo = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.before_request
@login_required
def antes_de_peticion():
    pass

# Listar alumnos
@alumnos_bp.route("/alumnos", methods=["GET"])
def listar_alumnos():
    alumnos = Alumnos.query.all()
    return render_template("alumnos.html", alumnos=alumnos)


# Crear alumno
@alumnos_bp.route("/alumnos/nuevo", methods=["GET", "POST"])
def nuevo_alumno():
    if request.method == "POST":
        alumno = Alumnos(
            nombre=request.form["nombre"],
            apellido=request.form["apellido"],
            edad=request.form["edad"],
            nota_1=request.form["nota_1"],
            nota_2=request.form["nota_2"],
            asistencia=request.form["asistencia"]
        )

        bd.session.add(alumno)
        bd.session.commit()

        return redirect(url_for("alumnos.listar_alumnos"))

    return render_template("agregar_alumno.html")


# Mostrar formulario de edición
@alumnos_bp.route("/alumnos/editar/<int:id>", methods=["GET"])
def mostrar_edicion(id):
    alumno = Alumnos.query.get_or_404(id)
    return render_template("editar_alumno.html", alumno=alumno)


# Actualizar alumno
@alumnos_bp.route("/alumnos/editar/<int:id>", methods=["POST"])
def actualizar_alumno(id):
    alumno = Alumnos.query.get_or_404(id)

    alumno.nombre = request.form["nombre"]
    alumno.apellido = request.form["apellido"]
    alumno.edad = request.form["edad"]
    alumno.nota_1 = request.form["nota_1"]
    alumno.nota_2 = request.form["nota_2"]
    alumno.asistencia = request.form["asistencia"]

    bd.session.commit()

    return redirect("/alumnos")


# Eliminar alumno
@alumnos_bp.route("/alumnos/eliminar/<int:id>", methods=["POST"])
def eliminar_alumno(id):
    alumno = Alumnos.query.get_or_404(id)

    bd.session.delete(alumno)
    bd.session.commit()

    return redirect("/alumnos")

@alumnos_bp.route("/predecir", methods=["GET", "POST"])
@login_required
def predecir():
    prediccion = None
    if request.method == "POST":
        nota_1 = float(request.form["nota_1"])
        nota_2 = float(request.form["nota_2"])
        asistencia = float(request.form["asistencia"])

        datos = np.array([[nota_1, nota_2, asistencia]])
        prediccion = round(modelo.predict(datos)[0], 2)

    return render_template("predecir.html", prediccion=prediccion)