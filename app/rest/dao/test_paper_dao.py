from flask import current_app
import rest.dao.mongodb as connection_manager
import rest.dao.mysqldb as connection_manager_mysql

import rest.utils.util as util
from bson.objectid import ObjectId

def post_tp(data):
	current_app.logger.debug("Entering method add_user of test_paper_dao.")
	db, connection = connection_manager.get_connection()
	result = db.tp.insert_one(data)
	connection_manager.close_connection(connection)
	current_app.logger.debug("Exit method add_user of test_paper_dao.")
	try:
		dbmysql = connection_manager_mysql.get_connection()
		cursor = dbmysql.cursor()
		sql = "insert into tp (tpid,name,updated_by) values ( %s,%s,%s);"
		cursor.execute(sql, (str(result.inserted_id), data['name'],'sys',))
		dbmysql.commit()
	except Exception, e:
		current_app.logger.error("Exception : %s", e)
		dbmysql.rollback()
		# something unexpected happed.
	return result.inserted_id

def publish_tp(tpid):
	current_app.logger.debug("Entering method publish tp of test_paper_dao.")
	db, connection = connection_manager.get_connection()
	fltr = { '_id': ObjectId(tpid)}
	data = {
	"$set": {
	"status": "status"
	}
	}
	result = db.tp.update_one(fltr,data)
	current_app.logger.debug("Exit method publish tp of test_paper_dao.")

def invite_user_for_test(data):
	current_app.logger.debug("Entering method publish tp of test_paper_dao.")
	db, connection = connection_manager.get_connection()
	result = db.tp_usr.insert_one(data)
	current_app.logger.debug("Exit method publish tp of test_paper_dao.")
