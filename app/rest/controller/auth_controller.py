from flask import Flask, Blueprint, jsonify, request, current_app, session
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.auth_validator as validator
import rest.dao.auth_dao as auth_dao
import rest.utils.gobal_variable as gobal_variable


#blueprint object for auth conthtroller
blueprint = Blueprint('auth_controller', __name__)

@blueprint.route('/authenticate/', methods=['POST'])
def authenticate():
	"""
	Method validates user name and password. 
	Set user id in session if authentications is success. 
	"""
	current_app.logger.debug("Entering method authenticate of auth_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.authenticate(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', None)
	return_value = auth_dao.authenticate(data)
	if return_value != -1:
		status_code = http_status_codes.SUCCESS
		status_message = "success"
		data['uid'] = return_value
		#setting user is authenicated user in gobal logged in list.
		if not data['uid'] in gobal_variable.user_logged_in_list:
			gobal_variable.user_logged_in_list.append(data['uid'])
			print "adding ......"
			print gobal_variable.user_logged_in_list
		return_data =  data
	else:
		status_code = http_status_codes.UNAUTHORIZED
		status_message = "Authentication failed. Username or password doesn't match"
		data["password"] = ""
		return_data =  data
	current_app.logger.debug("Exit method authenticate.")
	return util.to_json(status_code, status_message, return_data)


@blueprint.route('/logout/<uid>/', methods=['POST'])
def logout(uid):
	"""
	Method logsout and removes user information from gobal logged in list.
	"""
	if uid in gobal_variable.user_logged_in_list:
		del gobal_variable.user_logged_in_list[uid]
	status_code = http_status_codes.SUCCESS
	status_message = "success"
	return_data = None
	return util.to_json(status_code, status_message, return_data)


