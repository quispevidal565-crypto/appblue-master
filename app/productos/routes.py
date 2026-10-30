from flask import Blueprint, render_template

productos_bp = Blueprint('productos',__name__,url_prefix='/productos',template_folder='templates')

@productos_bp.route("/")
def lista_productos():
    return render_template('index.html')


@productos_bp.route("/categorias/<categoria>")
def mostrar_categorias(categoria):
    return f"<h3>Lista de productos de la categoria: {categoria} </h3>"
