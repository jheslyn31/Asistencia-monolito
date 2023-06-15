from flask import Blueprint, render_template

bp = Blueprint('equipo', __name__, url_prefix='/equipo')

@bp.route('/create')
def create():
    return 'crear equipo'

@bp.route('/update')
def update():
    return 'actualizar equipo'

@bp.route('/delete')
def delete():
    return 'eliminar equipo'