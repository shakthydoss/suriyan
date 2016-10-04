from flask import current_app
import rest.dao.mysqldb as connection_manager
import rest.utils.util as util
import rest.utils.gobal_variable as gobal_variable
import requests


def authenticate(data):
	current_app.logger.debug("Entering method authenticate of auth_dao.")
	r = requests.post('http://localhost/auth/authenticateUser/', data = data)
	print r.status_code
	
	return ""

def is_logged_in(uid):
	if uid in gobal_variable.user_logged_in_list:
		return True
	else:
		return False
