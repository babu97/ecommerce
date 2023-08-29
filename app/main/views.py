from flask import render_template, session, redirect, request, url_for
from . import main

main.route("/")


def index():
    return render_template("<h1>testing</h2>")
