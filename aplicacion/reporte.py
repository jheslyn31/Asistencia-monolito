from flask import Blueprint, jsonify

bp = Blueprint('reporte', __name__, url_prefix='/reporte')


@bp.route('/list', methods=["GET"])
def list():
    data = [
        {"nombre": "Romel", "fecha": "10/10/2022", "horae": "9:05",
            "horas": "17:05", "estado": 1, "justi": ""},
        {"nombre": "PEdrito", "fecha": "10/10/2022", "horae": "9:05",
            "horas": "17:05", "estado": 3, "justi": "justi1"},
        {"nombre": "Eduardito", "fecha": "10/10/2022", "horae": "9:05",
            "horas": "17:05", "estado": 3, "justi": "justi2"},
        {"nombre": "Telmito", "fecha": "10/10/2022", "horae": "9:05",
            "horas": "17:05", "estado": 2, "justi": ""}
    ]
    return jsonify(data)
