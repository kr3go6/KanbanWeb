from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("index.html")


@auth.route("/sign_up")
def sign_up():
    return "<p>Sign Up</p>"
