from flask import Blueprint, render_template

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/asistencia')
def index():
    return "Lista de tareas"

@bp.route('/reporte')
def reporte():
    return render_template('todo/reporte.html')

@bp.route('/persona')
def persona():
    return render_template('todo/persona.html')