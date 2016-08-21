from flask import current_app
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util

def add_user(data):
	current_app.logger.debug("Entering method add_user of user_management_dao.")
	db = connection_manager_mysql.get_connection()
	cursor = db.cursor()
	sql = "select * from usr where username = %s;" 
	cursor.execute(sql, (data['username'],))
	results  = cursor.fetchall()
	return_value = ""
	if(results):
		# user already exit.
		return_value = 1  
	else:
		try:
			uid = util.get_key()
			current_ts = util.get_current_ts()
			sql = "insert into usr (uid,username,updated_date,updated_by) values ( %s, %s,%s,%s);"
			cursor.execute(sql, (uid, data['username'], current_ts,data['access_token'],))
			sql = "insert into secret (uid,secret,updated_date,updated_by) values ( %s, %s,%s,%s);"
			cursor.execute(sql, (uid, data['password'],current_ts,data['access_token'],))
			db.commit()
			# return user id upon successful creation.
			return_value = uid
		except Exception, e:
			current_app.logger.error("Exception : %s", e)
			db.rollback()
			return_value = -1
	connection_manager_mysql.close_db(db)
	current_app.logger.debug("Exit method add_user of user_management_dao.")
	return return_value

def add_role(data):
	current_app.logger.debug("Entering method add_role of user_management_dao.")
	db = connection_manager_mysql.get_connection()
	cursor = db.cursor()
	role_ids = data['role_ids']
	try:
		# delete all current role.
		sql = "delete from usr_role where uid = %s;"
		cursor.execute(sql, (data['uid'],))
		for role_id in role_ids:
			# assign new role.
			sql = "insert into usr_role (uid, role_id, updated_by) values ( %s, %s, %s);"
			cursor.execute(sql, (data['uid'], role_id, data['access_token'],))
		db.commit()
	except Exception, e:
		current_app.logger.error("Exception : %s", e)
		db.rollback()
		# something unexpected happed.
		return_value = -1
	current_app.logger.debug("Exit method add_role of user_management_dao.")

