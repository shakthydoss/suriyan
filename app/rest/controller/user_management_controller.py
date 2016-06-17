from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.user_management_validator as validator
import rest.dao.user_management_dao as user_management_dao


#blueprint object for home controller
blueprint = Blueprint('user_management_controller', __name__)

@blueprint.route('/user/add/', methods=["POST"])
def add_user():
	current_app.logger.debug("Entering method add_user of user_management_controller.")
	data = request.json
	is_valid, error = validator.add_user(data)
	if not (is_valid):
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	registered = user_management_dao.add_user(data)
	status_code = None
	return_data = None
	status_message = ""
	if (registered == 1):
		# user already exit. 
		status_code = http_status_codes.CONFLICT
		status_message = "user already exit"
	elif (registered == -1):
		# something expected happend.
		status_code = http_status_codes.SERVER_ERROR
		status_message = "something unexpected happend"
	else:
		status_code = http_status_codes.SUCCESSFULLY_CREATED
		status_message = "success"
		data['user_id'] = registered
		return_data =  data
	current_app.logger.debug("Exit method add_user of user_management_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/user/role/', methods=["POST"])
def add_role():
	current_app.logger.debug("Entering method add_role of user_management_controller.")
	data = request.json
	is_valid = validator.add_role(data)
	if not (is_valid):
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	out = user_management_dao.add_role(data)
	status_code = None
	return_data = None
	status_message = ""
	if (out == -1):
		# something expected happend.
		status_code = http_status_codes.SERVER_ERROR
		status_message = "something unexpected happend"
	else:
		status_code = http_status_codes.SUCCESSFULLY_CREATED
		status_message = "success"
	current_app.logger.debug("Exit method add_user of user_management_controller.")
	return util.to_json(status_code, status_message, return_data)
