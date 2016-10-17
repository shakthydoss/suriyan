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
        return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input')
    return_data = test_paper_dao.get_tp_by_id(tpid)
    current_app.logger.debug("Exit method get_tp_by_id of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, return_data)


# uploads the test paper and saves as draft
@blueprint.route('/tp/', methods=['POST'])
def post_tp():
    current_app.logger.debug("Entering method post_tp of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.post_tp(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    data = request.json
    tpid = test_paper_dao.post_tp(data)
    current_app.logger.debug("Exit method post_tp of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESSFULLY_CREATED, str(tpid))


# gets all test paper by uid
@blueprint.route('/tp/uid/<uid>/', methods=['GET'])
def get_tp_by_uid(uid):
    current_app.logger.debug("Entering method get_tp_by_uid of test_paper_controller.")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    return_data = test_paper_dao.get_tp_by_uid(uid)
    current_app.logger.debug("Exit method get_tp_by_uid of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, return_data)


@blueprint.route('/tp/create/', methods=['POST'])
def create_tp():
    current_app.logger.debug("Entering method create_tp of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.create_tp(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    tpid = test_paper_dao.create_tp(data)
    tmp = dict()
    tmp["tpid"] = str(tpid)
    status_code = 200
    current_app.logger.debug("Exiting method create_tp of test_paper_controller.")
    return util.to_json(status_code, tmp)


@blueprint.route('/tp/addQuestion/', methods=['POST'])
def add_question_to_tp():
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.add_question_to_tp(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_paper_dao.add_question_to_tp(data)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/tp/updateQuestion/', methods=['POST'])
def update_question_to_tp():
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_question_to_tp(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_paper_dao.update_question_to_tp(data)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/tp/removeQuestion/', methods=['POST'])
def remove_question_from_tp():
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.remove_question_from_tp(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_paper_dao.remove_question_from_tp(data)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/tp/updateTag/', methods=['POST'])
def update_tags():
    current_app.logger.debug("Entering method update_tags of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_tags(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_paper_dao.update_tags(data)
    current_app.logger.debug("Exiting method update_tags of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/tp/updateStatus/', methods=['POST'])
def update_status():
    current_app.logger.debug("Entering method update_tags of test_paper_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_status(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    test_paper_dao.update_status(data)
    current_app.logger.debug("Exiting method update_tags of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)

@blueprint.route('/tp/inviteUserForTest/<tpid>/<uid>/', methods=['GET'])
def invite_user_for_test(tpid, uid):
    current_app.logger.debug("Entering method invite_user_for_test of test_paper_controller.")
    if not tpid:
        return util.to_json(http_status_codes.BAD_REQUEST, "tpid cannot be empty")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    test_paper_dao.invite_user_for_test(tpid, uid)
    current_app.logger.debug("Exit method post_tp of test_paper_controller.")
    return util.to_json(http_status_codes.SUCCESSFULLY_CREATED, None)

# create_tp(name, created_by)
# add_question_to_tp(tpip, question)
# update_question_to_tp(tpip,question)
# remove_question_from_tp(tpip,question)
# delete_tp(tpid)
# update_status(tpid, status)
# update_tags(tpid, tags)
