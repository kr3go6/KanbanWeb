from flask import Blueprint
from flask import redirect, url_for, request
from flask import render_template
from flask_login import current_user
from app import db
from datetime import datetime
from .models import User, Kanban

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect(url_for("auth.login"))


@views.route("/board")
def board():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    
    user = User.query.filter_by(email=current_user.email, 
            password_hash=current_user.password_hash).first()
    

    if user:
        todos = Kanban.query.filter_by(uid=user.id, type=0)
        inprogs = Kanban.query.filter_by(uid=user.id, type=1)
        dones = Kanban.query.filter_by(uid=user.id, type=2)
    
        return render_template("board.html", todos=todos, inprogs=inprogs, dones=dones)

    return render_template("board.html")

@views.route("/add_kanban", methods=["GET", "POST"])
def add_kanban():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    
    user = User.query.filter_by(email=current_user.email, 
            password_hash=current_user.password_hash).first()
    
    if user:
        if request.method == "POST":
            kb_text = request.form.get("new_kanban")

            if kb_text == "":
                return redirect(url_for("views.board"))

            kb_type = request.form.get("kb_type")
            
            if kb_type not in ("to_do", "in_progress", "done"):
                return redirect(url_for("views.board"))

            kb_type = ("to_do", "in_progress", "done").index(kb_type)

            new_kanban = Kanban(uid=current_user.id,
                    type=kb_type, content=kb_text, create_time=datetime.now())
            db.session.add(new_kanban)
            db.session.commit()

    return redirect(url_for("views.board"))

@views.route("/delete_kanban/<id>", methods=["GET", "POST"])
def delete_kanban(id):
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    kanban = Kanban.query.filter_by(id=id).first()

    if kanban:
        db.session.delete(kanban)
        db.session.commit()

    return redirect(url_for("views.board"))
