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
                 "VALUES (?, ?, ?, ?, ?)", list(item_dict.values()))
    conn.commit()


def get_product(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Product WHERE id = ?", (product_id,))
    result = c.fetchall()
    return result[0]


def update_product(product, index):
    product = list(product.values())
    conn = sqlite3.connect('database.db')
    conn.execute("UPDATE Product SET name = ? WHERE id = ?",
                 (product[0], index))
    conn.execute("UPDATE Product SET quantity = ? WHERE id = ?",
                 (product[1], index))
    conn.execute("UPDATE Product SET price = ? WHERE id = ?",
                 (product[2], index))
    conn.execute("UPDATE Product SET provider = ? WHERE id = ?",
                 (product[3], index))
    conn.execute("UPDATE Product SET provider_contact = ? WHERE id = ?",
                 (product[4], index))
    conn.commit()
