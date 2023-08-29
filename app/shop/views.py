from flask import render_template, session, redirect, request, url_for
from . import shop

shop.route("/")


def home():
    return "Home page of your shop"
