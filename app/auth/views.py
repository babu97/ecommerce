from flask import render_template, session, redirect, request, url_for, flash
from app import db, bycrypt
from .forms import RegistationForm, LoginForm
from ..models import User
from ..decorators import logout_required
from flask_login import current_user, login_user, login_required, logout_user
from . import auth
from werkzeug.security import check_password_hash

from ..email import send_email


@logout_required
@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thank you for registering,You can now Login", category="success")
        return redirect(url_for(".login"))

    return render_template("auth/register.html", form=form)


@logout_required
@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next is None or not next.startswith("/"):
                next = url_for("main.index")
                flash("You have succesfully  Logged In", category="success")
            return redirect(next)
        flash("Invalid email or password.", category="danger")
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", category="warning")
    return redirect(url_for("main.index"))


@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for("main.index"))
    if current_user.confirm(token):
        db.session.commit()
        flash("You have confirmed your account.Thanks!", category="success")
    else:
        flash("The confirmation link is invalid or has expired.", category="danger")
    return redirect(url_for("main.index"))


@auth.route("/confirm")
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(
        current_user.email,
        "Confirm You Account",
        "auth/email/confirm",
        user=current_user,
        token=token,
    )
    return redirect(url_for("main.index"))


@auth.before_app_request
def before_request():
    if (
        current_user.is_authenticated
        and not current_user.confirmed
        and request.blueprint != "auth"
        and request.endpoint != "static"
    ):
        return redirect(url_for("auth.unconfirmed"))


@auth.route("/unconfirmed")
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for("main.index"))
    return render_template("auth/unconfirmed.html")
