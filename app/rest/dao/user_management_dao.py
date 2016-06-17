from flask import current_app
import rest.dao.mysqldb as connection_manager
import rest.utils.util as util

def add_user(data):
	current_app.logger.debug("Entering method add_user of user_management_dao.")
	db = connection_manager.get_connection()
	cursor = db.cursor()
	sql = "select * from usr where email = %s;" 
	cursor.execute(sql, (data['email'],))
	results  = cursor.fetchall()
	return_value = ""
	if(results):
		# user already exit.
		return_value = 1  
	else:
		try:
			uid = util.get_key()
			sql = "insert into usr (uid,name,email,updated_by) values ( %s, %s,%s,%s);"
			cursor.execute(sql, (uid, data['name'], data['email'], 'sys',))
			sql = "insert into secret (uid,secret,updated_by) values ( %s, %s,%s);"
			cursor.execute(sql, (uid, data['secret'],'sys',))
			db.commit()
			# return user id upon successful creation.
			return_value = uid
		except Exception, e:
			current_app.logger.error("Exception : %s", e)
			db.rollback()
			# something unexpected happed.
			return_value = -1
	connection_manager.close_db(db)
	current_app.logger.debug("Exit method add_user of user_management_dao.")
	return return_value

def add_role(data):
	current_app.logger.debug("Entering method add_role of user_management_dao.")
	db = connection_manager.get_connection()
	cursor = db.cursor()
	role_ids = data['role_ids']
	try:
		# delete all current role.
		sql = "delete from usr_role where uid = %s;"
		cursor.execute(sql, (data['uid'],))
		for role_id in role_ids:
			# assign new role.
			sql = "insert into usr_role (uid, role_id, updated_by) values ( %s, %s, %s);"
			cursor.execute(sql, (data['uid'], role_id, "sys",))
		db.commit()
	except Exception, e:
		current_app.logger.error("Exception : %s", e)
		db.rollback()
		# something unexpected happed.
		return_value = -1
	current_app.logger.debug("Exit method add_role of user_management_dao.")

