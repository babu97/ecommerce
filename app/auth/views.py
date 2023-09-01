from flask import render_template, session, redirect, request, url_for, flash
from app import db, bycrypt
from .forms import RegistationForm, LoginForm
from ..models import User
from ..decorators import logout_required
from flask_login import current_user, login_user,login_required
from . import auth
from werkzeug.security import check_password_hash




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
        flash("Invalid email or password.")
    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
