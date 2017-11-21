#!/usr/bin/env python
import sqlite3

from bottle import FormsDict

from db_utils import Table


class Product(Table):
    """A Product table of an item database."""

    table_name = 'Product'
    primary_key = 'id'

    def get_by_name(self, name) -> sqlite3.Row:
        """Fetch a Product row by its 'name' field.

        :param: the name of the product to find
        :return: a row of the found product
        """
        return self.get(name, key='name')


class Order(Table):
    """An Order table of an item database."""

    table_name = '"Order"'
    primary_key = 'id'

    def update_total(self, order_id: int, total: float):
        self.update(('total', total), (self.primary_key, order_id))


class OrderLine(Table):
    """An OrderLine table of an item database."""

    table_name = 'OrderLine'
    primary_key = 'id'

    def _create_orderline_row(self, form: FormsDict):
        """Helper method to create OrderLine row."""
        product = Product(self.db)
        product_row = product.get_by_name(form['name'])

        if product_row is None:
            raise sqlite3.DatabaseError("Product not found.")

        cost = int(form['quantity']) * product_row['price']
        return {'product_id': product_row['id'],
                'price': product_row['price'],
                'quantity': int(form['quantity']),
                'cost': cost}

    def _update_order_total(self, cost: float, order_id: int):
        """Helper method to update the 'total' field of an Order table."""
        order = Order(self.db)
        order_row = order.get(order_id)
        total = order_row['total'] + cost
        order.update_total(order_id, total)

    def add_by_form(self, form: FormsDict, order_id: int):
        """Add a row using data from a POST request form."""
        orderline_row = self._create_orderline_row(form)
        self._update_order_total(orderline_row['cost'], order_id)
        self.add(orderline_row)

    def receipt(self, order_id: int):
        query = ('SELECT Product.name, OrderLine.quantity, OrderLine.price,'
                 '    OrderLine.cost '
                 'FROM OrderLine '
                 'JOIN Product ON Product.id = OrderLine.product_id '
                 'WHERE order_id = ? ORDER BY OrderLine.id')
        return self.db.fetchall(query, (order_id,))