#!/usr/bin/env python
"""Provides simple database lookup methods."""
from model import Customer, Employee, Order, Product


def customer_by_id(customer_id, db):
    return db.query(Customer).get(customer_id)


def customer_by_name(customer, db):
    return db.query(Customer).filter_by(name=customer).first()


def employee_by_id(employee_id, db):
    return db.query(Employee).get(employee_id)


def employee_by_name(employee, db):
    return db.query(Employee).filter_by(name=employee).first()


def order_by_id(order_id, db):
    return db.query(Order).get(order_id)


def product_by_id(product_id, db):
    return db.query(Product).get(product_id)


def product_by_name(product, db):
    return db.query(Product).filter_by(name=product).first()
