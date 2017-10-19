#!/usr/bin/env python
import bottle
from bottle import template, static_file, view
from bottle_sqlalchemy import Plugin
from sqlalchemy import create_engine
import db_utils
from model import Base
import os

css_path = os.getcwd() + '/static/css'
engine = create_engine("sqlite:///data.db", echo=True)
sqlalchemy_plugin = Plugin(engine, Base.metadata, create=True)
app = bottle.Bottle()
app.install(sqlalchemy_plugin)


@app.route("/")
def index():
    return template("index")

@app.route('/views/modify.tpl')
def modify():
    return template('modify.tpl', root='./views/', table=db_utils.format_table())


@app.route("/static/<filename>")
def send_static(filename):
    return static_file(filename, root=css_path)


if __name__ == "__main__":
    app.run(debug=True, port=8080, reloader=True)
