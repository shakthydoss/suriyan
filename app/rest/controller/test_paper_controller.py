from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.test_paper_validator as validator
import rest.dao.test_paper_dao as test_paper_dao

#blueprint object for home controller
blueprint = Blueprint('test_paper_controller', __name__)

# method to publish the test paper. 
@blueprint.route('/tp/', methods=['GET'])
def get_tps():
	return jsonify({'message': 'return all tps'})

# method to publish the test paper. 
@blueprint.route('/tp/tpid/<tpid>/', methods=['GET'])
def get_tp_by_id(tpid):
	current_app.logger.debug("Entering method get_tp_by_id of test_paper_controller.")
	return_data = test_paper_dao.get_tp_by_id(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	current_app.logger.debug("Exit method get_tp_by_id of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

# uploads the test paper and saves as draft
@blueprint.route('/tp/', methods=['POST'])
def post_tp():
	current_app.logger.debug("Entering method post_tp of test_paper_controller.")
	data = request.json
	is_valid, error = validator.post_tp(data)
	if not (is_valid):
		return util.to_json(http_status_codes.BAD_REQUEST, error, None)
	_id = test_paper_dao.post_tp(data)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = str(_id)
	current_app.logger.debug("Exit method post_tp of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

# method to publish the test paper. 
@blueprint.route('/tp/tpid/<tpid>/publish', methods=['POST'])
def publish(tpid):
	test_paper_dao.publish_tp(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	return util.to_json(status_code, status_message, return_data)


@blueprint.route('/tp/inviteUserForTest/<tpid>/<user_id>',  methods=['GET'])
def invite_user_for_test(tpid, user_id):
	current_app.logger.debug("Entering method invite_user_for_test of test_paper_controller.")
	data = {
	"tpid": tpid,
	"user_id" : user_id,
	"last_update_ts": util.get_current_ts_in_ms(),
	"completed":"n",
	"started":"n"
	}
	test_paper_dao.invite_user_for_test(data)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method post_tp of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/tp/tpid/<tpid>/deactivate', methods=['POST'])
def deactivate(tpid):
	current_app.logger.debug("Extering method deactivate of test_paper_controller.")
	test_paper_dao.deactivate(tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	current_app.logger.debug("Exit method deactivate of test_paper_controller.")
	return util.to_json(status_code, status_message, return_data)
