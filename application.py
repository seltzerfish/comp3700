#!/usr/bin/env python
import bottle
from bottle import template, static_file, view, redirect, request, post
import db_utils
import os

css_path = os.getcwd() + '/static/css'
app = bottle.Bottle()

@app.route('/', method='POST')
def add_product():
    db_utils.add_new_product(request.forms)
    redirect('/modify')

@app.route("/")
def index():
    return template("index")

@app.route('/modify')
def modify():
    return template('modify.tpl', root='./views/', table=db_utils.return_table())

@app.route('/add')
def add():
    return template('add.tpl', root='./views/')

@app.route('/update/<index>', method='POST')
def update_item(index):
    db_utils.update_product(request.forms, index)
    redirect('/modify')

@app.route('/delete/<index>')
def delete(index):
    db_utils.delete_product(index)
    redirect('/modify')

@app.route('/update/<index>')
def update_item(index):
    data = db_utils.get_product(index)
    return template('update.tpl', root='./views/', item_data=data)

@app.route("/static/<filename>")
def send_static(filename):
    return static_file(filename, root=css_path)


if __name__ == "__main__":
    app.run(debug=True, port=8080, reloader=True)
