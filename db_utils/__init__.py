#!/usr/bin/env python
import sqlite3


def connect_db(name):
    return sqlite3.connect(f'db/{name}')


class SQLiteDatabase:
    def __init__(self, name):
        self.connection = connect_db(name)

    def execute(self, query, params=tuple()):
        with self.connection as conn:
            return conn.execute(query, params)

    def executemany(self, query, seq_of_params):
        with self.connection as conn:
            return conn.executemany(query, seq_of_params)

    def fetchone(self, query, params=tuple()):
        c = self.execute(query, params)
        return c.fetchone()

    def fetchall(self, query, params=tuple()):
        c = self.execute(query, params)
        return c.fetchall()

    def get_table(self, table):
        self.fetchall('SELECT * FROM ?',
                      (table,))

    def get_row(self, table, key, value):
        self.fetchone('SELECT * FROM ? WHERE ? = ?',
                      (table, key, value))

    def add_default_row(self, table):
        self.execute('INSERT INTO ? DEFAULT VALUES',
                     (table,))

    def update_row(self, table, field, data, key, value):
        self.execute('UPDATE ? SET ? = ? WHERE ? = ?',
                     (table, field, data, key, value))

    def update_row_from_form(self, form, table, key, value):
        values = [(table, field, data, key, value)
                  for field, data in form.items()]
        self.executemany('UPDATE ? SET ? = ? WHERE ? = ?',
                         values)

    def delete_row(self, table, column, value):
        self.execute('DELETE FROM ? WHERE ? = ?',
                     (table, column, value))
