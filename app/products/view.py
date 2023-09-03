from . import products
from flask import redirect, render_template, url_for, flash, request
from app.models import db
from .form import NameForm, Addproducts, CategoryForm
from app.models import Brand, Category
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import IntegrityError  # Import IntegrityError from SQLAlchemy


@products.route("/addbrand", methods=["GET", "POST"])
def addbrand():
    form = NameForm()
    if form.validate_on_submit():
        brand = Brand(name=form.name.data)
        try:
            db.session.add(brand)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()  # Rollback the transaction in case of IntegrityError
            flash("A brand with the same name already exists.", category="warning")
        else:
            flash(f"Brand { brand.name } added successfully", category="success")
            return redirect(url_for(".addbrand"))
    return render_template("products/addbrand.html", form=form,)


@products.route("/addcategory", methods=["GET", "POST"])
def addcategory():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()  # Rollback the transaction in case of IntegrityError
            flash("A Category with the same name already exists.", category="warning")
        else:
            flash(f"category { category.name }added successfully", category="success")
            return redirect(url_for(".addcategory"))
    return render_template("products/addbrand.html", form=form)

@products.route('/addproduct', methods = ['GET','POST'])

