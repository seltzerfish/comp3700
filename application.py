#!/usr/bin/env python
import bottle
from bottle import template, static_file, view, request, redirect
from bottle_sqlalchemy import Plugin
from sqlalchemy import create_engine

from model import Base
from form import ProductForm

engine = create_engine("sqlite:///database.db", echo=True)
sqlalchemy_plugin = Plugin(engine, Base.metadata, create=True)

app = bottle.Bottle()
app.install(sqlalchemy_plugin)


@app.route("/", name="index")
def index():
    return template("index")


@app.route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root='/static/')


@app.route("/product", method=["GET", "POST"], name="new_product")
def add_product():
    form = ProductForm(request.forms)
    if request.method == "POST" and form.validate():
        # TODO: Add product to database.
        pass
    elif request.method == "POST" and not form.validate():
        return template("product.tpl", form=form, errors=form.errors)
    return template("product.tpl", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=8080, reloader=True)
