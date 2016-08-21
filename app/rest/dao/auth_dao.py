from flask import current_app
import rest.dao.mysqldb as connection_manager
import rest.utils.util as util
import rest.utils.gobal_variable as gobal_variable


def authenticate(data):
	current_app.logger.debug("Entering method authenticate of auth_dao.")
	db = connection_manager.get_connection()
	cursor = db.cursor()
	sql = "select usr.uid from usr, secret where usr.uid = secret.uid and secret.secret = %s and usr.username = %s;"
	cursor.execute(sql, (data['password'],data['username'],))
	results  = cursor.fetchone()
	if(results):
		# valid used
		return_value = results[0]
	else:
		# not exist
		return_value = -1
	current_app.logger.debug("Exit method authenticate of auth_dao.")
	return return_value

def is_logged_in(uid):
	if uid in gobal_variable.user_logged_in_list:
		return True
	else:
		return False
