#!/usr/bin/env python
from bottle_sqlalchemy import Plugin
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=True)
sqlalchemy_plugin = Plugin(engine, Base.metadata, create=True)


def row_as_dict(row):
    """Transform a row from a table into a dict.

    Adapted from https://stackoverflow.com/a/37350445
    """
    d = {}
    for col in inspect(row).mapper.column_attrs:
        d[col.key] = getattr(row, col.key)
    return d
