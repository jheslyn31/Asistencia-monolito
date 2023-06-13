from flask import Flask, render_template, url_for



def create_app():
    app= Flask(__name__)

    #configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY= 'dev'
    )

    #Registrar Bluprint
    from . import  todo
    app.register_blueprint(todo.bp)

    # Crear aplicación de flask
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app