from flask import current_app
import rest.dao.mysqldb as connection_manager
import rest.utils.util as util

def register(data):
	current_app.logger.debug("Entering method register of auth_dao.")
	db = connection_manager.get_connection()
	cursor = db.cursor()
	sql = "select * from urs where email = %s;" 
	cursor.execute(sql, (data['email'],))
	results  = cursor.fetchall()
	return_value = ""
	if(results):
		# user already exit.
		return_value = 1  
	else:
		try:
			uid = util.get_key()
			sql = "insert into urs (uid,name,email) values ( %s, %s,%s);"
			cursor.execute(sql, (uid, data['name'], data['email'],))
			sql = "insert into secret (uid,secret) values ( %s, %s);"
			cursor.execute(sql, (uid, data['secret'],))
			db.commit()
			# return user id upon successful creation.
			return_value = uid
		except Exception, e:
			current_app.logger.error("Exception : %s", e)
			db.rollback()
			# something unexpected happed.
			return_value = -1
	connection_manager.close_db(db)
	current_app.logger.debug("Exit method register of auth_dao.")
	return return_value

