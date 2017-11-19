import sqlite3


def connect_db():
    return sqlite3.connect('db/user_database.db')

def validate_user(username, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM User WHERE Username = \"{}\"".format(username))
    u = c.fetchone()
    c.close()
    print(u)

