from flask import Blueprint
from flask import redirect, url_for
from flask import render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect(url_for("auth.login"))


@views.route("/board")
def board(nickname="World"):
    return render_template("board.html", name=nickname)
