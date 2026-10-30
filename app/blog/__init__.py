from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.admin.routes import admin_bp
    from app.blog.routes import blog_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)

    return app