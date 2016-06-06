from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.dao.auth_dao as auth_dao

#blueprint object for auth conthtroller
blueprint = Blueprint('auth_controller', __name__)

@blueprint.route('/authenticate/', methods=['GET'])
def authenticate():
	current_app.logger.debug("Entering method authenticate of auth_controller.")
	#do something here
	current_app.logger.debug("Exit method authenticate.")
	return jsonify({'message': 'This is authenticate'}), http_status_codes.SUCCESS

@blueprint.route('/register/', methods=["POST"])
def register():
	current_app.logger.debug("Entering method register of auth_controller.")
	data = request.json
	register = auth_dao.register(data)
	status_code = None
	return_data = None
	message = ""
	if (register == 1):
		# user already exit. 
		status_code = http_status_codes.CONFLICT
		message = "user already exit"
	elif (register == -1):
		# something expected happend.
		status_code = http_status_codes.SERVER_ERROR
		message = "something unexpected happend"
	else:
		status_code = http_status_codes.SUCCESSFULLY_CREATED
		message = "success"
		return_data = {'user_id':register}
	current_app.logger.debug("Exit method register of auth_controller.")
	return jsonify({'status' : status_code, 'message': message, 'data': return_data }), status_code

