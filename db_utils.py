import sqlite3

def format_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, id, quantity, price, provider, provider_contact FROM Product ORDER BY id")
    result = c.fetchall()
    return result

def delete_product(index):
    conn = sqlite3.connect('database.db')
    conn.execute("DELETE FROM Product WHERE id = " + str(index))
    conn.commit()
