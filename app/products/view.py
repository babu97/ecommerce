from . import products
from flask import redirect, render_template, url_for, flash, request
from app.models import db
from .form import nameForm
from app.models import Brand
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import IntegrityError  # Import IntegrityError from SQLAlchemy


@products.route("/addbrand", methods=["GET", "POST"])
def addbrand():
    form = nameForm()
    if form.validate_on_submit():
        brand = Brand(name=form.name.data)
        try:
            db.session.add(brand)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()  # Rollback the transaction in case of IntegrityError
            flash("A brand with the same name already exists.", category="warning")
        else:
            flash("Brand added successfully", category="success")
            return redirect(url_for(".addbrand"))
    return render_template("products/addbrand.html", form=form)
