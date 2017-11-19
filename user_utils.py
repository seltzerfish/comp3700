import sqlite3


def connect_db():
    return sqlite3.connect('db/user_database.db')

def is_valid_login(username, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT Password FROM User WHERE Username = \"{}\"".format(username))
    p = c.fetchone()
    c.close()
    if p and p[0] == password:
        return True
    return False

def get_user_permissions(username):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT Permissions FROM User WHERE Username = \"{}\"".format(username))
    p = c.fetchone()
    c.close()
    return p[0]
