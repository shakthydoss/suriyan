import rest.dao.test_dao as test_dao
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.test_validator as validator
from flask import Blueprint, request, current_app

blueprint = Blueprint('test_controller', __name__)


# get all testpaper assinged for the user
@blueprint.route('/test/mytestpaper/<uid>/', methods=['GET'])
def my_testpaper(uid):
    current_app.logger.debug("Entering method my_testpaper of test_paper_controller.")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    result = test_dao.my_testpaper(uid)
    current_app.logger.debug("Exiting method my_testpaper of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, result)


@blueprint.route('/test/started/<tpid>/<uid>/', methods=['GET'])
def test_started(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    test_dao.test_started(tpid, uid)
    current_app.logger.debug("Exiting method test_started of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/test/updateResponse/', methods=['POST'])
def update_response():
    current_app.logger.debug("Entering method update_responce of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_response(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_dao.update_response(data)
    current_app.logger.debug("Exiting method update_responce of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/test/removeResponse/', methods=['POST'])
def remove_response():
    current_app.logger.debug("Entering method removeResponse of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.remove_response(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_dao.remove_response(data)
    current_app.logger.debug("Exiting method remove_response of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/test/completed/<tpid>/<uid>/', methods=['GET'])
def test_completed(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    test_dao.evaluate_result(tpid, uid)
    test_dao.test_completed(tpid, uid)
    current_app.logger.debug("Exiting method test_started of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/test/evaluateResult/<tpid>/<uid>/', methods=['GET'])
def evaluate_result(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    test_dao.evaluate_result(tpid, uid)
    current_app.logger.debug("Exiting method test_started of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/test/summary/<tpid>/<uid>/', methods=['GET'])
def get_summary_test(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    result = test_dao.get_summary_test(tpid, uid)
    return util.to_json(http_status_codes.SUCCESS, result)


@blueprint.route('/load-test/<tpid>/<uid>/', methods=['GET'])
def load_test(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    result = test_dao.get_summary_test(tpid, uid)
    return util.to_json(http_status_codes.SUCCESS, result)
