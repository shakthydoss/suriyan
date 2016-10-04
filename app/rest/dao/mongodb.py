from pymongo import MongoClient


def get_connection():
    connection = MongoClient()
    db = connection.suriyan  # db = connection['suriyan']
    return db, connection


def close_connection(connection):
    if connection:
        connection.close()
