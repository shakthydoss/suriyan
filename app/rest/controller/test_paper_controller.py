from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.test_paper_validator as validator
import rest.dao.test_paper_dao as test_paper_dao

# blueprint object for home controller
blueprint = Blueprint('test_paper_controller', __name__)

# method to get all the test paper. 
@blueprint.route('/tp/', methods=['GET'])
def get_tps():
	return jsonify({'message': 'return all tps'})

# method to publish the test paper. 
@blueprint.route('/tp/tpid/<tpid>/', methods=['GET'])
def get_tp_by_id(tpid):
	current_app.logger.debug("Entering method get_tp_by_id of test_paper_controller.")
	if not tpid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	return_data = test_paper_dao.get_tp_by_id(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	current_app.logger.debug("Exit method get_tp_by_id of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

# uploads the test paper and saves as draft
@blueprint.route('/tp/', methods=['POST'])
def post_tp():
	current_app.logger.debug("Entering method post_tp of test_paper_controller.")
	if hasattr(request, 'json'):
		data = request.json
		is_valid, error = validator.post_tp(data)
		if not (is_valid):
			return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	else:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', None)
	data = request.json
	_id = test_paper_dao.post_tp(data)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = str(_id)
	current_app.logger.debug("Exit method post_tp of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

# method to publish the test paper. 
@blueprint.route('/tp/tpid/<tpid>/publish', methods=['POST'])
def publish(tpid):
	current_app.logger.debug("Entering method post_tp of test_paper_controller.")
	if not tpid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	test_paper_dao.publish_tp(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method post_tp of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)


@blueprint.route('/tp/inviteUserForTest/<tpid>/<uid>',  methods=['GET'])
def invite_user_for_test(tpid, uid):
	current_app.logger.debug("Entering method invite_user_for_test of test_paper_controller.")
	if not tpid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	if not uid:
		return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input', error)
	test_paper_dao.invite_user_for_test(tpid, uid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method post_tp of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/tp/tpid/<tpid>/deactivate', methods=['POST'])
def deactivate(tpid):
	current_app.logger.debug("Entering method deactivate of test_paper_controller.")
	test_paper_dao.deactivate(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method deactivate of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

#gets all test paper by uid
@blueprint.route('/tp/uid/<uid>', methods=['GET'])
def get_tp_by_uid(tpid,uid):
	current_app.logger.debug("Entering method deactivate of test_paper_controller.")
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method deactivate of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)