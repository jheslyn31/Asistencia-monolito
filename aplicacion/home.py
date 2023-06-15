from flask import Blueprint, render_template

bp = Blueprint('home', __name__)


@bp.route('/')
def login():
    return render_template('auth/login.html')


@bp.route('/asistencia')
def asistencia():
    return render_template('asistencia.html')


@bp.route('/reporte')
def reporte():
    return render_template('reporte.html')


@bp.route('/persona')
def persona():
    return render_template('persona.html')
