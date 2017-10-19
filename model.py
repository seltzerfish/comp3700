#!/usr/bin/env python
from sqlalchemy import func, Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer(), primary_key=True)

    name = Column(String(length=30), nullable=False)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)

    name = Column(String(length=30), nullable=False)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True)

    name = Column(String(length=30), nullable=False)
    quantity = Column(Integer())
    price = Column(Numeric(precision=9, scale=2))
    provider = Column(String(length=30))
    provider_contact = Column(String(length=12))


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)

    customer_id = Column(Integer(), ForeignKey('customers.id'))
    employee_id = Column(Integer(), ForeignKey('employees.id'))
    total = Column(Numeric(precision=9, scale=2))
    date = Column(DateTime(), server_default=func.current_timestamp())


class OrderLine(Base):
    __tablename__ = 'orderlines'
    id = Column(Integer(), primary_key=True)

    product_id = Column(Integer(), ForeignKey('products.id'), nullable=False)
    order_id = Column(Integer(), ForeignKey('orders.id'), nullable=False)
    quantity = Column(Integer())
    price = Column(Numeric(precision=9, scale=2))
    total = Column(Numeric(precision=9, scale=2))
