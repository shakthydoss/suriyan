from flask import Flask, Blueprint, jsonify, request, current_app, session
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.tag_validator as validator
import rest.dao.tag_dao as tag_dao
import rest.utils.gobal_variable as gobal_variable


#blueprint object for auth conthtroller
blueprint = Blueprint('tag_controller', __name__)

@blueprint.route('/tags/', methods=['GET'])
def get_tags():
	current_app.logger.debug("Entering method get_tags of tag_controller.")
	return_data = tag_dao.get_tags()
	status_code = 200
	status_message = "Success"
	current_app.logger.debug("Exit method get_tags of tag_controller.")
	return util.to_json(status_code, return_data)

@blueprint.route('/tag/id/<tag_id>/', methods=['GET'])
def get_tag_by_id(tag_id):
	current_app.logger.debug("Entering method get_tag_by_id of tag_controller.")
	return_data = tag_dao.get_tag_by_id(tag_id)
	status_code = 200
	status_message = "Success"
	current_app.logger.debug("Exit method get_tag_by_id of tag_controller.")
	return util.to_json(status_code, return_data)


@blueprint.route('/tag/new/', methods=['POST'])
def save_tag():
	current_app.logger.debug("Entering method save_tag of tag_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.save_tag(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, None)

	return_value = tag_dao.save_tag(data)
	return_data = None
	status_code = 200
	status_message = "Success"
	if(return_value != 0):
		return_data = None
		status_code = 400
		status_message = "Tag name already exit or could not process you request"
	current_app.logger.debug("Exit method save_tag of tag_controller.")
	return util.to_json(status_code, return_data)

@blueprint.route('/tag/update/', methods=['POST'])
def update_tag():
	current_app.logger.debug("Entering method save_tag of tag_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.update_tag(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, None)

	return_value = tag_dao.update_tag(data)
	return_data = None
	status_code = 200
	status_message = "Success"
	if(return_value != 0):
		return_data = None
		status_code = 400
		status_message = "Tag name already exit or could not process you request"
	current_app.logger.debug("Exit method save_tag of tag_controller.")
	return util.to_json(status_code, return_data)