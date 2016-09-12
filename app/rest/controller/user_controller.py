from flask import Flask, Blueprint, jsonify, request, current_app, session
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.user_validator as validator
import rest.dao.user_dao as user_dao
import rest.dao.auth_dao as auth_dao
import rest.utils.gobal_variable as gobal_variable

#blueprint object for auth conthtroller
blueprint = Blueprint('user_controller', __name__)

@blueprint.route('/changePassword/', methods=['Post'])
def change_password():
	"""
	Method checks if user is active and updates the new password for login.
	"""
	current_app.logger.debug("Entering method change_password of user_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.change_password(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', None)
	data = request.json
	if auth_dao.is_logged_in(data['access_token']) == False:
		return util.to_json(http_status_codes.UNAUTHORIZED, 'Not Authorized', None)
	return_value = user_dao.change_password(data)
	status_code = None
	status_message = None
	return_data = None
	if return_value == 1:
		status_code = 200
		status_message = "Success"
		return_data = None
	if return_value == -1:
		status_code = 400
		status_message = "Bad Request"
		return_data = None
	current_app.logger.debug("Exit method change_password of user_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/changeUsername/', methods=['Post'])
def change_username():
	"""
	Method changes the username
	"""
	current_app.logger.debug("Entering method change_username of user_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.change_username(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', None)
	data = request.json
	if auth_dao.is_logged_in(data['access_token']) == False:
		return util.to_json(http_status_codes.UNAUTHORIZED, 'Not Authorized', None)
	status_code = None
	status_message = None
	return_data = None
	return_value = user_dao.change_username(data)
	if return_value == 1:
		status_code = 200
		status_message = "success"
		return_data = None
	if return_value == -1:
		status_code = 400
		status_message = data['new_username'] +" is not avaiable. or could't process the request."
		return_data = None
	current_app.logger.debug("Exit method change_username of user_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/getRole/uid/<uid>/', methods=['GET'])
def get_role_for_user(uid):
	"""
	Method gets all roles assiged for the user. 
	"""
	current_app.logger.debug("Entering method get_role_for_user of user_controller.")
	if not uid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	return_value, list_roles = user_dao.get_role_for_user(uid)
	if return_value == 1:
		status_code = 200
		status_message = "success"
		return_data = { 'roles':list_roles }
	if return_value == -1:
		status_code = 400
		status_message = "Bad Request"
		return_data = None
	current_app.logger.debug("Exit method get_role_for_user of user_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/updateProfile/', methods=['POST'])
def update_my_profile():
	"""
	Method validates and updates user profile details like full name, email, phone, etc. 
	"""
	current_app.logger.debug("Entering method of update_my_profile of user_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.update_my_profile(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', None)
	data = request.json
	if auth_dao.is_logged_in(data['access_token']) == False:
		return util.to_json(http_status_codes.UNAUTHORIZED, 'Not Authorized', None)
	user_dao.update_my_profile(data)
	return_data = None
	status_code = 200
	status_message = "success"
	current_app.logger.debug("Exit method of update_my_profile of user_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/getProfile/uid/<uid>/', methods=['GET'])
def get_my_profile(uid):
	"""
	Method retrieves user saved profile details from the database.
	"""
	current_app.logger.debug("Entering method of update_my_profile of user_controller.")
	if not uid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	return_data = user_dao.get_my_profile(uid)
	status_code = 200
	status_message = "success"
	current_app.logger.debug("Exit method of update_my_profile of user_controller.")
	return util.to_json(status_code, status_message, return_data)



