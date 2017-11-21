#!/usr/bin/env python
from bottle import FormsDict
import sqlite3
from typing import Any, ClassVar, Iterable, List, Tuple


def connect_db(name: str) -> sqlite3.Connection:
    """Connect to an SQLite database.

    :param name: filename of an SQLite database
    :return: an SQLite database connection

    .. note:: Attaches an sqlite3.Row row factory to the connection to allow
        indexing of fetched rows.
    """
    conn = sqlite3.connect(f'db/{name}')
    conn.row_factory = sqlite3.Row
    return conn


class SQLiteDatabase:
    """An SQLite database controller."""
    def __init__(self, name):
        self.connection = connect_db(name)

    def execute(self, query: str, params: Iterable=()) -> sqlite3.Cursor:
        """Executes an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :return: a cursor over the result of the execution
        """
        with self.connection as conn:
            return conn.execute(query, params)

    def executemany(self, query: str,
                    seq_of_params: Iterable[Iterable]=()) -> sqlite3.Cursor:
        """Executes an SQLite query multiple times with different parameters.

        Similar to :func:`~dbutils.SQLitedatabase.execute`, but performed over
        every set of parameters in `seq_of_params`.

        :param query: an SQLite query
        :param seq_of_params: a sequence of sets of query parameters
        :return: a cursor over the result of the execution
        """
        with self.connection as conn:
            return conn.executemany(query, seq_of_params)

    def fetchone(self, query: str, params: Iterable=()) -> sqlite3.Row:
        """Fetches one row from an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :return: a single row fetched from an SQLite query
        """
        c = self.execute(query, params)
        return c.fetchone()

    def fetchall(self, query: str, params: Iterable=()) -> List[sqlite3.Row]:
        """Fetches all rows from an SQLite query.

        :param query: an SQLite query
        :param params: a set of query parameters (in order)
        :return: all rows fetched from an SQLite query
        """
        c = self.execute(query, params)
        return c.fetchall()

    def get_table(self, table: str, desc: bool=False) -> List[sqlite3.Row]:
        """Fetches all rows from a specified table in the database.

        :param table: case-sensitive name of the table
        :param desc: if `True`, table will be ordered by descending ROWID
        :return: all rows from specified table in database
        """
        query, params = 'SELECT * FROM ?', (table,)
        if desc:
            query = 'SELECT * FROM ? ORDER BY ?.ROWID DESC'
            params = (table, table)
        return self.fetchall(query, params)

    def get_row(self, table: str, key: Tuple[str, Any]) -> sqlite3.Row:
        """Fetches a row from a specified table in the database.

        :param table: case-sensitive name of the table
        :param key: `tuple` (name, value) pair for the primary key
        :return: a row matching the provided key pair
        """
        return self.fetchone('SELECT * FROM ? WHERE ? = ?',
                             (table, *key))

    def add_default_row(self, table: str):
        """Adds a row with default values into the specified table.

        :param table: case-sensitive name of the table
        """
        self.execute('INSERT INTO ? DEFAULT VALUES',
                     (table,))

    def update_row_from_form(self, form: FormsDict, table: str,
                             key: Tuple[str, Any]):
        """Updates a row in the specified table using a POST request form.

        :param form: POST request form containing table data
        :param table: case-sensitive table name
        :param key: `tuple` (name, value) pair for the primary key
        """
        values = []
        for field, data in form.items():
            values.append((table, field, data, *key))
        self.executemany('UPDATE ? SET ? = ? WHERE ? = ?', values)



class Table:
    """A base class for database tables."""
    table_name: ClassVar[str] = str()
    primary_key: ClassVar[str] = str()

    def __init__(self, db: SQLiteDatabase):
        self.db = db

    def get(self, rowid: Any) -> sqlite3.Row:
        return self.db.get_row(self.table_name, (self.primary_key, rowid))

    def get_by(self, key: Tuple[str, Any]):
        return self.db.get_row(self.table_name, key)

    def update(self, field: Tuple[str, Any], key: Tuple[str, Any]):
        """Updates a row in the specified table in the database.

        :param field: `tuple` (name, value) pair for the updated field
        :param key: `tuple` (name, value) pair for the primary key
        """
        self.db.execute('UPDATE ? SET ? = ? WHERE ? = ?',
                        (self.table_name, *field, *key))

    def delete(self, rowid: Any):
        """Deletes a row from the table.

        :param rowid: `tuple` (name, value) pair for the primary key
        """
        self.db.execute('DELETE FROM ? WHERE ? = ?',
                        (self.table_name, *rowid))
