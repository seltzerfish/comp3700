#!/usr/bin/env python
import bottle
from bottle import template, static_file, redirect, request, get, post, route
from beaker.middleware import SessionMiddleware
from cork import Cork, AuthException
from cork.backends import SQLiteBackend

import db_utils

sbe = SQLiteBackend('db/database.db')
sbe.connection.executescript("""
    INSERT INTO users (username, desc, role, creation_date) VALUES
    (
        'admin',
        'admin test user',
        'admin',
        '2017-11-14 20:18:00.000000'
    );
    INSERT INTO roles (role, level) VALUES ('admin', 100);
    INSERT INTO roles (role, level) VALUES ('manager', 60);
    INSERT INTO roles (role, level) VALUES ('cashier', 50);
""")
aaa = Cork(backend=sbe, initialize=True)
app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'TEST KEY PLEASE IGNORE',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True
}
app = SessionMiddleware(app, session_opts)


@get('/login', name='login')
@post('/login')
def login():
    if request.method == 'POST':
        username = request.forms['username']
        password = request.forms['password']
        aaa.login(username, password,
                  success_redirect='/',
                  fail_redirect='/login')

    return {}  # TODO: Make login form.


@route('/logout', name='logout')
def logout():
    aaa.logout(success_redirect='/login')


@post('/create_user')
def create_user():
    try:
        username = request.forms['username']
        role = request.forms['role']
        password = request.forms['password']
        aaa.create_user(username, role, password)
        return {'ok': True, 'msg': ''}
    except AuthException as e:
        return {'ok': False, 'msg': e}


@route('/', name='index')
def index():
    return template('index')


@route('/orders', name='order_list')
def order_list():
    table = db_utils.order_table()
    new_id = table[0][0] + 1
    return template('orders', table=table, new_id=new_id)


@route('/order/<order_id:int>', name='order_receipt')
def order_receipt(order_id):
    table = db_utils.orderline_table(order_id)
    return template('order', table=table, order_id=order_id)


@get('/add/order/<order_id:int>', name='add_order')
@post('/add/order/<order_id:int>')
def add_order(order_id):
    if not db_utils.get_order(order_id):
        # Create order if it does not exist.
        db_utils.add_order()
    if request.method == 'POST':
        # Add item to order.
        result = db_utils.add_orderline(request.forms, order_id)
        return template('add-order', added=result, order_id=order_id,
                        item=request.forms)
    return template('add-order', order_id=order_id)


@get('/add/product', name='add_product')
@post('/add/product')
def add_product():
    if request.method == 'POST':
        db_utils.add_new_product(request.forms)
        redirect(app.get_url('product_list'))
    return template('add-product')


@route('/products', name='product_list')
def product_list():
    table = db_utils.product_table()
    return template('products', table=table)


@get('/update/<product_id:int>', name='update_product')
@post('/update/<product_id:int>')
def update_product(product_id):
    if request.method == 'POST':
        db_utils.update_product(request.forms, product_id)
        redirect(app.get_url('product_list'))
    data = db_utils.get_product(product_id)
    return template('update', item_data=data)


@get('/delete/<product_id:int>', name='delete_product')
def delete_product(product_id):
    db_utils.delete_product(product_id)
    redirect(app.get_url('product_list'))


@route('/denied', name='denied')
def denied():
    return {}  # TODO: Make "sorry, you're unauthorized" page.


@route("/static/<file:path>")
def send_static(file):
    return static_file(file, root='static/')


if __name__ == "__main__":
    app.run(port=8080)
