import MySQLdb
import time


def get_connection():
    db = MySQLdb.connect("localhost", "developer", "developer", "suriyan")
    return db


def close_db(db):
    if db:
        db.close()
