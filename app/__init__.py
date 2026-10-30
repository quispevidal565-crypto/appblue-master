from flask import Flask

def create_app():
    app = Flask(__name__)

    # Página principal
    @app.route("/")
    def inicio():
        return """
        <h1>Bienvenido a AppBlue</h1>
        <p>Proyecto Flask - Tecnologías Emergentes II</p>
        <a href="/panel">Panel administrativo</a><br>
        <a href="/entrada/1">Blog</a>
        """

    # Importar blueprints originales
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.auth.routes import auth_bp

    # Importar nuevos blueprints
    from app.admin.routes import admin_bp
    from app.blog.routes import blog_bp

    # Registrar todos los blueprints
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)

    return app