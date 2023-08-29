from flask import render_template, session, redirect, request, url_for
from . import main


@main.route("/")
def index():
    return ('printing')
