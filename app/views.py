from flask import Blueprint
from flask import redirect, url_for
from flask import render_template
from flask_login import current_user

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect(url_for("auth.login"))


@views.route("/board")
def board():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    return render_template("board.html")
