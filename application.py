#!/usr/bin/env python
import bottle
from bottle import template, static_file, view
from bottle_sqlalchemy import Plugin
from sqlalchemy import create_engine

from model import Base

engine = create_engine("sqlite:///database.db", echo=True)
sqlalchemy_plugin = Plugin(engine, Base.metadata, create=True)

app = bottle.Bottle()
app.install(sqlalchemy_plugin)


@app.route("/")
def index():
    return template("index")


@app.route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root='/static/')


if __name__ == "__main__":
    app.run(debug=True, port=8080, reloader=True)
