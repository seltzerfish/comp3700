import sqlite3


def product_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, id, quantity, price, provider, provider_contact "
              "FROM Product ORDER BY id")
    result = c.fetchall()
    return result


def delete_product(product_id):
    conn = sqlite3.connect('database.db')
    conn.execute("DELETE FROM Product WHERE id = ?", (product_id,))
    conn.commit()


def add_new_product(item_dict):
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO Product"
                 "    (name,quantity,price,provider,provider_contact) "
                 "VALUES (:name,:quantity,:price,:provider,:provider_contact)",
                 dict(item_dict))
    conn.commit()


def get_product(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Product WHERE id = ?", (product_id,))
    result = c.fetchall()
    return result[0]


def update_product(product, product_id):
    """Update a product in the database.

    :param FormsDict product: Product info form passed in from POST.
    :param int product_id: Product.id key used for database lookup.
    """
    conn = sqlite3.connect('database.db')
    conn.execute("UPDATE Product SET name = ? WHERE id = ?",
                 (product["name"], product_id))
    conn.execute("UPDATE Product SET quantity = ? WHERE id = ?",
                 (product["quantity"], product_id))
    conn.execute("UPDATE Product SET price = ? WHERE id = ?",
                 (product["price"], product_id))
    conn.execute("UPDATE Product SET provider = ? WHERE id = ?",
                 (product["provider"], product_id))
    conn.execute("UPDATE Product SET provider_contact = ? WHERE id = ?",
                 (product["provider_contact"], product_id))
    conn.commit()
