from flask import Blueprint, render_template

bp = Blueprint('asistencia', __name__, url_prefix='/asistencia')


@bp.route('/register')
def register():
    return 'registrar asistencia'

