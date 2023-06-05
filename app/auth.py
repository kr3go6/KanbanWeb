from flask import Blueprint, render_template, request, url_for, flash, redirect
from .models import User, Kanban
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("user_email") 
        password = request.form.get("user_password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash("Logged in succsessfully!", category="success")
                #  return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html")


@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("user_email")
        password = request.form.get("user_password")
        password1 = request.form.get("user_password1")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif password != password1:
            flash("Passwords don\"t match.", category="error")
        elif len(password) < 6:
            flash("Password must be at least 6 characters.", category="error")
        else:
            new_user = User(email=email, password_hash=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return render_template("login.html")
        
    return render_template("sign_up.html")
