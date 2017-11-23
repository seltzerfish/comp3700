#!/usr/bin/env python
from sqlite3 import DatabaseError

from db_utils import Table, SQLiteDatabase


class User:
    """User table of user database."""
    table_name = 'User'
    primary_key = 'Username'


class UserDatabase(SQLiteDatabase):
    """Controller for SQL user database."""

    def authorize(self, username):
        """Check the authorization of a given user.

        :param username: primary key of User table
        :type username: str
        :return: whether a given user has authorization
        :rtype: bool
        """
        user = User(self).get(username)
        if not user:
            raise DatabaseError("User does not exist.")
        return user['Permissions'] == 'MANAGER'

    def validate_login(self, username, password):
        """Validate a user login.

        :param username: primary key of User table
        :param password: password to verify
        :type username: str
        :type password: str
        :return: whether user login info is correct
        :rtype: bool
        """
        user = User(self).get(username)
        return user and user['Password'] == password
