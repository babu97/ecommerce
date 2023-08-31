from flask import render_template, session, redirect, request, url_for, flash
from app import db
from . import main
from .forms import RegistationForm
from ..models import User


@main.route("/register", methods=["GET", "POST"])
def index():
    form = RegistationForm()
    if request.method == "POST" and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        flash("Thank you for registering", category="success")
        return redirect(url_for(".login"))

    return render_template("auth/register.html", form=form)
