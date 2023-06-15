from flask import Flask, render_template, url_for


def create_app():

    # Crear aplicacion de flask
    app = Flask(__name__)

    # Registrar vistas
    from aplicacion import home
    app.register_blueprint(home.bp)

    from aplicacion import auth
    app.register_blueprint(auth.bp)

    from aplicacion import reporte
    app.register_blueprint(reporte.bp)

    from aplicacion import equipo
    app.register_blueprint(equipo.bp)

    return app
