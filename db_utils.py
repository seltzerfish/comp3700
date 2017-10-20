import sqlite3

def return_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, id, quantity, price, provider, provider_contact FROM Product ORDER BY id")
    result = c.fetchall()
    return result

def delete_product(product_id):
    conn = sqlite3.connect('database.db')
    conn.execute("DELETE FROM Product WHERE id = " + str(product_id))
    conn.commit()

def add_new_product(item_dict):
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO Product (name,quantity,price,provider,provider_contact) VALUES (?, ?, ?, ?, ?)", list(item_dict.values()))
    conn.commit()

def get_product(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Product WHERE id = " + str(product_id))
    result = c.fetchall()
    return result[0]

def update_product(product, index):
    product = list(product.values())
    conn = sqlite3.connect('database.db')
    conn.execute("UPDATE Product SET name = \'" + str(product[0]) + "\' WHERE id = " + index)
    conn.execute("UPDATE Product SET quantity = \'" + str(product[1]) + "\' WHERE id = " + index)
    conn.execute("UPDATE Product SET price = \'" + str(product[2]) + "\' WHERE id = " + index)
    conn.execute("UPDATE Product SET provider = \'" + str(product[3]) + "\' WHERE id = " + index)
    conn.execute("UPDATE Product SET provider_contact = \'" + str(product[4]) + "\' WHERE id = " + index)
    conn.commit()