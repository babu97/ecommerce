from flask import render_template, session, redirect, request, url_for,flash
from app import db
from . import main
from .forms import RegistationForm


@main.route("/register", methods=["GET", "POST"])
def index():
    form = RegistationForm()
    if request.method == 'POST' and  form.validate():
        flash('Thank you for registering')
        return redirect(url_for('login'))

    return render_template("register.html", form=form)
