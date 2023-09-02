from . import products
from flask import redirect, render_template, url_for, flash, request
from app.models import db
from .form import nameForm
from app.models import Brand


@products.route("/addbrand", methods=["GET", "POST"])
def addbrand():
    form = nameForm()
    if form.validate_on_submit():
        brand = Brand(name=form.name.data)
        db.session.add(brand)
        db.session.commit()
        flash("Brand added succesfully", category="success")
        return redirect(url_for("addbrand"))

    return render_template("products/addbrand.html")
