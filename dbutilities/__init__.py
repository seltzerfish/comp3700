#!/usr/bin/env python
from sqlalchemy import inspect


def row_as_dict(row):
    """Transform an SQLAlchemy Query row into a dict.

    Adapted from https://stackoverflow.com/a/37350445
    """
    d = {}
    for col in inspect(row).mapper.column_attrs:
        d[col.key] = getattr(row, col.key)
    return d
