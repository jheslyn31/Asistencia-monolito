from flask import Blueprint, render_template

bp = Blueprint('persona', __name__, url_prefix='/persona')

@bp.route('/create')
def create():
    return 'crear persona'

@bp.route('/update')
def update():
    return 'actualizar persona'

@bp.route('/delete')
def delete():
    return 'eliminar persona'