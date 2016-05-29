import MySQLdb
import time

def get_connection():
	db = MySQLdb.connect("localhost", "root", "admin", "suriyan")
	return db

def close_db(db):
	if db:
		db.close()

