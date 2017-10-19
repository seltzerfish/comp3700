def format_table():
    import sqlite3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, id, quantity, price, provider, provider_contact FROM Product ORDER BY id")
    result = c.fetchall()
    return result