#!/usr/bin/env python
import bottle

import dbutilities
import dbutilities.lookup

app = bottle.Bottle()
app.install(dbutilities.sqlalchemy_plugin)


@app.route('/static/<path:path>')
def static(path):
    """Serve static content."""
    return bottle.static_file(path, root='static/')


@app.get("/customer/<customer_id:int>")
def get_customer(customer_id, db):
    entity = dbutilities.lookup.customer_by_id(customer_id, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Customer ID#{customer_id} not found.")


@app.get("/customer/name/<customer>")
def get_customer(customer, db):
    entity = dbutilities.lookup.customer_by_name(customer, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Customer \"{customer}\" not found.")


@app.get("/employee/<employee_id:int>")
def get_employee(employee_id, db):
    entity = dbutilities.lookup.employee_by_id(employee_id, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Customer ID#{employee_id} not found.")


@app.get("/employee/name/<employee>")
def get_employee(employee, db):
    entity = dbutilities.lookup.employee_by_name(employee, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Employee \"{employee}\" not found.")


@app.get("/order/<order_id:int>")
def get_order(order_id, db):
    entity = dbutilities.lookup.order_by_id(order_id, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Product ID#{order_id} not found.")


@app.get("/product/<product_id:int>")
def get_product(product_id, db):
    entity = dbutilities.lookup.product_by_id(product_id, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Product ID#{product_id} not found.")


@app.get("/product/name/<product>")
def get_product(product, db):
    entity = dbutilities.lookup.product_by_name(product, db)
    if entity:
        return dbutilities.row_as_dict(entity)
    else:
        return bottle.HTTPError(404, f"Product \"{product}\" not found.")
