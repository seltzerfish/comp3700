#!/usr/bin/env python
import os

import bottle
from bottle import template, static_file, view, redirect, request, post

import db_utils

# TODO: Test on other computers before removing 'css_path'.
css_path = os.getcwd() + '/static/css'
app = bottle.Bottle()


@app.route('/', name='index')
def index():
    return template('index')


@app.get('/add', name='add_product')
@app.post('/add')
def add_product():
    if request.method == 'POST':
        db_utils.add_new_product(request.forms)
        redirect(app.get_url('product_table'))
    return template('add')


@app.route('/products', name='product_table')
def product_table():
    table = db_utils.product_table()
    return template('products', table=table)


@app.get('/update/<product_id:int>', name='update_product')
@app.post('/update/<product_id:int>')
def update_product(product_id):
    if request.method == 'POST':
        db_utils.update_product(request.forms, product_id)
        redirect(app.get_url('product_table'))
    data = db_utils.get_product(product_id)
    return template('update', item_data=data)


@app.get('/delete/<product_id:int>', name='delete_product')
def delete_product(product_id):
    db_utils.delete_product(product_id)
    redirect(app.get_url('product_table'))


@app.route("/static/<file:path>")
def send_static(file):
    return static_file(file, root='static/')


if __name__ == "__main__":
    app.run(debug=True, port=8080, reloader=True)
