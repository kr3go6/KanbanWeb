from flask import Blueprint, render_template, request, url_for, flash, redirect
from .models import User
from werkzeug.security import check_password_hash
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("login") 
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succsessfully!', category='success')
                #  return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')


    
    return render_template("index.html")


@auth.route("/sign_up")
def sign_up():
    return "<p>Sign Up</p>"
