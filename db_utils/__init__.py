#!/usr/bin/env python
import abc
import sqlite3
from typing import Iterable

from bottle import FormsDict


def connect_db(name):
    """Connect to an SQLite database.

    :param name: filename of an SQLite database
    :type name: str
    :return: an SQLite database connection
    :rtype: sqlite3.Connection

    .. note:: Attaches an :class:`sqlite3.Row` row factory to the connection to
        allow indexing of fetched rows.
    """
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn


class SQLiteDatabase:
    """An SQLite database controller."""

    def __init__(self, name):
        self.connection = connect_db(name)

    def execute(self, query, params=()):
        """Executes an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :type query: str
        :type params: Iterable
        :return: a cursor over the result of the execution
        :rtype: sqlite3.Cursor
        """
        with self.connection as conn:
            return conn.execute(query, params)

    def executemany(self, query, seq_of_params=()):
        """Executes an SQLite query multiple times with different parameters.

        Similar to :func:`~db_utils.SQLiteDatabase.execute`, but performed over
        every set of parameters in `seq_of_params`.

        :param query: an SQLite query
        :param seq_of_params: a sequence of sets of query parameters
        :type query: str
        :type seq_of_params: Iterable[Iterable]
        :return: a cursor over the result of the execution
        """
        with self.connection as conn:
            return conn.executemany(query, seq_of_params)

    def fetchone(self, query, params=()):
        """Fetches one row from an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :type query: str
        :type params: Iterable
        :return: a single row fetched from an SQLite query
        :rtype: sqlite3.Row
        """
        c = self.execute(query, params)
        return c.fetchone()

    def fetchall(self, query, params=()):
        """Fetches all rows from an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :type query: str
        :type params: Iterable
        :return: all rows fetched from an SQLite query
        :rtype: list[sqlite3.Row]
        """
        c = self.execute(query, params)
        return c.fetchall()


class Table(metaclass=abc.ABCMeta):
    """An abstract base class for SQLite database tables.

    :cvar table_name: name of the table in the database
    :cvar primary_key: name of the primary key of the table
    :ivar db: the :class:`~db_utils.SQLiteDatabase` object to use as a
        connection to the SQLite database
    :type table_name: str
    :type primary_key: str
    :type db: SQLiteDatabase
    """

    table_name = str()
    primary_key = str()

    def __init__(self, db):
        self.db = db

    def get(self, value, key=primary_key):
        """Fetches a row from the table.

        :param value: the key value of the row to fetch
        :param key: (default: :attr:`~db_utils.Table.primary_key`) the field
            to use as a key
        :type value: int | float | str | bytes
        :type key: str
        :return: a row matching the provided key
        :rtype: sqlite3.Row
        """
        return self.db.fetchone('SELECT * FROM ? WHERE ? = ?',
                                (self.table_name, key, value))

    def get_all(self, descending=False):
        """Fetches all rows from a specified table in the database.

        :param descending: if `True`, rows will be ordered by descending ROWID
        :type descending: bool
        :return: all rows from specified table in database
        :rtype: list[sqlite3.Row]
        """
        query, params = 'SELECT * FROM ?', (self.table_name,)
        if descending:
            query = 'SELECT * FROM ? ORDER BY ROWID DESC'
            params = (self.table_name,)
        return self.db.fetchall(query, params)

    def add(self, row):
        """Adds a row into the table.

        :param row: the row to add to the table, in dict form
        :type row: dict[str, int | float | str | bytes]
        """
        sub_marks = ','.join(['?'] * len(row))
        query = 'INSERT INTO ? ({sub_marks}) VALUES ({sub_marks})'
        query = query.format(sub_marks=sub_marks)
        params = (self.table_name, *row.keys(), *row.values())
        self.db.execute(query, params)

    def add_default(self):
        """Adds a row with default values into the table."""
        self.db.execute('INSERT INTO ? DEFAULT VALUES', (self.table_name,))

    def update(self, field, value, key=primary_key):
        """Updates a row in the specified table in the database.

        :param field: `tuple` (name, value) pair for the updated field
        :param value: the key value of the row to delete
        :param key: (default: :attr:`~db_utils.Table.primary_key`) the field
            to use as a key
        :type field: tuple[str, int | float | str | bytes]
        :type value: int | float | str | bytes
        :type key: str
        """
        self.db.execute('UPDATE ? SET ? = ? WHERE ? = ?',
                        (self.table_name, *field, key, value))

    def update_from_form(self, form, value, key=primary_key):
        """Updates a row in the specified table using a POST request form.

        :param form: POST request form containing row data
        :param value: the key value of the row to delete
        :param key: (default: :attr:`~db_utils.Table.primary_key`) the field
            to use as a key
        :type form: FormsDict
        :type value: int | float | str | bytes
        :type key: str
        """
        values = []
        for field, data in form.items():
            values.append((self.table_name, field, data, key, value))
        self.db.executemany('UPDATE ? SET ? = ? WHERE ? = ?', values)

    def delete(self, value, key=primary_key):
        """Deletes a row from the table.

        :param value: the key value of the row to delete
        :param key: (default: :attr:`~db_utils.Table.primary_key`) the field
            to use as a key
        :type value: int | float | str | bytes
        :type key: str
        """
        self.db.execute('DELETE FROM ? WHERE ? = ?',
                        (self.table_name, key, value))

    def thing(self):
        pass
