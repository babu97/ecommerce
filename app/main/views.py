from flask import render_template, session, redirect, request, url_for, flash,current_app
from . import main
from app import db
from ..models import User
from ..decorators import logout_required
from flask_login import current_user,login_required


@main.route("/", methods=["GET", "POST"])
def index():
  return  render_template('index.html')