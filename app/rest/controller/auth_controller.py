from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util

#blueprint object for auth conthtroller
blueprint = Blueprint('auth_controller', __name__)

@blueprint.route('/authenticate/', methods=['POST'])
def authenticate():
	current_app.logger.debug("Entering method authenticate of auth_controller.")
	print("I am here")
	data = request.json
	print(data)
	#do something here
	current_app.logger.debug("Exit method authenticate.")
	return jsonify({'message': 'This is authenticate'}), http_status_codes.SUCCESS



