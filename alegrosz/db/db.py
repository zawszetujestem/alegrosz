import sqlite3
import os

from flask import g


def get_db():
    """singleton pattern

    :return:
    """
    db = getattr(g, "_database", None)

    if db is None:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        db = g._database = sqlite3.connect(os.path.join(base_dir, 'alegrosz.db'))

    return db
