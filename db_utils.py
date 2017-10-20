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