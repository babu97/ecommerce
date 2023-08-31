from flask import render_template, session, redirect, request, url_for, flash
from app import db, bycrypt
from .forms import RegistationForm, LoginForm
from ..models import User
from ..decorators import logout_required
from flask_login import current_user, login_user
from . import auth


@logout_required
@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistationForm()
    if request.method == "POST" and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        flash("Thank you for registering,You can now Login", category="success")
        return redirect(url_for(".login"))

    return render_template("auth/register.html", form=form)


@logout_required
@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.data.email).first()
        if user is not None and bycrypt.check_password_hash(
            user.password, form.data.password
        ):
            login_user(user)
            next_page = request.args.get("next")
            if not next_page or not next.startswitch("/"):
                next_page = url_for("main.index")
        else:
            flash(
                "The email and password combination you entered is incorrect. Please try again or reset your password if need",
                category="danger",
            )
    return render_template("auth/login.html", form=form)
