from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.dao.auth_dao as auth_dao
import rest.validator.auth_controller_validator as validator

#blueprint object for auth conthtroller
blueprint = Blueprint('auth_controller', __name__)

@blueprint.route('/authenticate/', methods=['GET'])
def authenticate():
	current_app.logger.debug("Entering method authenticate of auth_controller.")
	#do something here
	current_app.logger.debug("Exit method authenticate.")
	return jsonify({'message': 'This is authenticate'}), http_status_codes.SUCCESS

@blueprint.route('/auth/register/', methods=["POST"])
def register():
	current_app.logger.debug("Entering method register of auth_controller.")
	data = request.json
	print(data['dasdas'])
	is_valid, error = validator.register(data)
	if not (is_valid):
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	register = auth_dao.register(data)
	status_code = None
	return_data = None
	status_message = ""
	if (register == 1):
		# user already exit. 
		status_code = http_status_codes.CONFLICT
		status_message = "user already exit"
	elif (register == -1):
		# something expected happend.
		status_code = http_status_codes.SERVER_ERROR
		status_message = "something unexpected happend"
	else:
		status_code = http_status_codes.SUCCESSFULLY_CREATED
		status_message = "success"
		data['user_id'] = register
		return_data =  data
	current_app.logger.debug("Exit method register of auth_controller.")
	return util.to_json(status_code, status_message, return_data)


