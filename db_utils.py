import sqlite3


def connect_db():
    return sqlite3.connect('db/item_database.db')


def execute(query, params=tuple()):
    conn = connect_db()
    conn.execute(query, params)
    conn.commit()


def fetchone(query, params=tuple()):
    conn = connect_db()
    c = conn.cursor()
    c.execute(query, params)
    result = c.fetchone()
    c.close()
    return result


def fetchall(query, params=tuple()):
    conn = connect_db()
    c = conn.cursor()
    c.execute(query, params)
    result = c.fetchall()
    c.close()
    return result


def order_table():
    return fetchall("SELECT * FROM \"Order\" ORDER BY id DESC")


def add_order():
    execute("INSERT INTO \"Order\" DEFAULT VALUES")


def get_order(order_id):
    return fetchone("SELECT * FROM \"Order\" WHERE id = ?", (order_id,))


def orderline_table(order_id):
    return fetchall("SELECT Product.name, OrderLine.quantity, OrderLine.price,"
                    "    OrderLine.cost "
                    "FROM OrderLine "
                    "JOIN Product ON Product.id = OrderLine.product_id "
                    "WHERE order_id = ? ORDER BY OrderLine.id", (order_id,))


def add_orderline(item, order_id):
    result = fetchone("SELECT * FROM Product WHERE name = ?", (item["name"],))

    if result is None:
        # Item not found.
        return False

    product_id = result[0]
    price = result[3]
    total = int(item["quantity"]) * price

    # Update order total.
    result = fetchone("SELECT total FROM \"Order\" WHERE id = ?", (order_id,))
    new_total = result[0] + total
    execute("UPDATE \"Order\" SET total = ? WHERE id = ?",
            (new_total, order_id))

    # Add order line.
    execute("INSERT INTO OrderLine"
            "    (order_id, product_id, quantity, price, cost) "
            "VALUES (?, ?, ?, ?, ?)",
            (order_id, product_id, item["quantity"], price, total))

    return True


def product_table():
    return fetchall("SELECT name, id, quantity, price, provider, "
                    "    provider_contact "
                    "FROM Product ORDER BY id")


def delete_product(product_id):
    execute("DELETE FROM Product WHERE id = ?", (product_id,))


def add_new_product(item_dict):
    execute("INSERT INTO Product"
            "    (name,quantity,price,provider,provider_contact) "
            "VALUES (:name,:quantity,:price,:provider,:provider_contact)",
            dict(item_dict))


def get_product(product_id):
    return fetchone("SELECT * FROM Product WHERE id = ?", (product_id,))


def update_product(product, product_id):
    """Update a product in the database.

    :param FormsDict product: Product info form passed in from POST.
    :param int product_id: Product.id key used for database lookup.
    """
    execute("UPDATE Product SET name = ? WHERE id = ?",
            (product["name"], product_id))
    execute("UPDATE Product SET quantity = ? WHERE id = ?",
            (product["quantity"], product_id))
    execute("UPDATE Product SET price = ? WHERE id = ?",
            (product["price"], product_id))
    execute("UPDATE Product SET provider = ? WHERE id = ?",
            (product["provider"], product_id))
    execute("UPDATE Product SET provider_contact = ? WHERE id = ?",
            (product["provider_contact"], product_id))
