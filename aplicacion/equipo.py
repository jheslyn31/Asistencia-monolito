from flask import Blueprint, render_template
from config import engine
from sqlalchemy import text 

bp = Blueprint('equipo', __name__, url_prefix='/equipo')

@bp.route("/")
def listar_equipos():
    query = """
        select idequipo, nombre from equipo 
    """
    conn = engine.connect()
    rs = conn.execute(text(query)).fetchall()
    data = []
    for i in rs:
        obj = {
            "idequipo": i[0],
            "nombre": i[1],            
        }
        data.append(obj)
    conn.close()
    print (data)
    return render_template("equipo.html", lista_equipos=data)   
