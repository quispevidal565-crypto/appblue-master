from flask import Blueprint, render_template

admin_bp = Blueprint(
    "admin",
    __name__,
    template_folder="templates"
)

@admin_bp.route("/panel")
def panel():
    return render_template("panel.html")