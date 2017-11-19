#!/usr/bin/env python
import bottle
from bottle import template, static_file, redirect, request, get, post, route
from beaker.middleware import SessionMiddleware
# from cork import Cork, AuthException
# from cork.backends import SQLiteBackend
import user_utils
import db_utils

# sbe = SQLiteBackend('db/user_database.db')
# aaa = Cork(backend=sbe, initialize=True)
session_opts = {
    'session.cookie_expires': 300,
    'session.encrypt_key': 'TEST KEY PLEASE IGNORE',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'memory',
    'session.validate_key': True,
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)


def get_session():
    return bottle.request.environ.get('beaker.session')


@get('/login', name='login')
@post('/login')
def login():
    s = get_session()
    if request.method == 'POST':
        username = request.forms['username']
        password = request.forms['password']
        if user_utils.is_valid_login(username, password):
            s["username"] = username
            s["permissions"] = user_utils.get_user_permissions(username)
            redirect("/")
        else:
            return template('invalid_login', sess=get_session())
    return template('login', sess=get_session())


@get('/update_profile/self')
@post('/update_profile/self')
def update_profile():
    if request.method == 'POST':
        s = get_session()
        username = s["username"]
        current_password = request.forms['current_password']
        new_password = request.forms['new_password']
        if (current_password and new_password and
                user_utils.is_valid_login(username, current_password)):
            user_utils.update_password(username, new_password)
            return template('update_profile_success', sess=s)
        else:
            return template('update_profile_fail', sess=s)
    return template('update_profile', sess=get_session())


@route('/logout', name='logout')
def logout():
    s = get_session()
    if "username" in s:
        del s["username"]
        del s["permissions"]
    redirect("/")


@route('/user/<user_id:int>', name='user_page')
def user(user_id):
    return {}  # TODO: Create user page.


@post('/change_password')
def change_password():
    aaa.current_user.update(pwd=request.forms['password'])


@post('/change_picture')
def change_picture():
    pass  # TODO: Change profile picture.


@route('/admin', name='admin')
def admin():
    aaa.require(role='manager', fail_redirect='/sorry')
    return {}  # TODO: Create admin page.


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
    s = bottle.request.environ.get('beaker.session')
    if 'username' not in s:
        redirect("/login")
    else:
        return template('index', sess=get_session())


@route('/orders', name='order_list')
def order_list():
    table = db_utils.order_table()
    new_id = table[0][0] + 1
    return template('orders', table=table, new_id=new_id, sess=get_session())


@route('/order/<order_id:int>', name='order_receipt')
def order_receipt(order_id):
    table = db_utils.orderline_table(order_id)
    return template('order', table=table, order_id=order_id, sess=get_session())


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
                        item=request.forms, sess=get_session())
    return template('add-order', order_id=order_id, sess=get_session())


@get('/add/product', name='add_product')
@post('/add/product')
def add_product():
    if request.method == 'POST':
        db_utils.add_new_product(request.forms)
        redirect('/products')

    return template('add-product', sess=get_session())


@route('/products', name='product_list')
def product_list():
    table = db_utils.product_table()
    return template('products', table=table, sess=get_session())


@get('/update/<product_id:int>', name='update_product')
@post('/update/<product_id:int>')
def update_product(product_id):
    if request.method == 'POST':
        db_utils.update_product(request.forms, product_id)
        redirect('/products')
    data = db_utils.get_product(product_id)
    return template('update', item_data=data, sess=get_session())


@get('/delete/<product_id:int>', name='delete_product')
def delete_product(product_id):
    db_utils.delete_product(product_id)
    redirect('/products')


@route('/denied', name='denied')
def denied():
    return {}  # TODO: Make "sorry, you're unauthorized" page.


@route("/static/<file:path>")
def send_static(file):
    return static_file(file, root='static/')


if __name__ == "__main__":
    bottle.run(app=app, host='localhost', port=8080, reloader=True, debug=True)
