import rest.dao.user_management_dao as user_management_dao
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.user_management_validator as validator
from flask import Blueprint, request, current_app

blueprint = Blueprint('user_management_controller', __name__)


@blueprint.route('/user/add/', methods=["POST"])
def add_user():
    current_app.logger.debug("Entering method add_user of user_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.add_user(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    data = request.json
    uid = user_management_dao.add_user(data)
    return_data = {"uid": uid}
    current_app.logger.debug("Exit method add_user of user_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, return_data)


@blueprint.route('/user/edit/', methods=["POST"])
def edit_user():
    current_app.logger.debug("Entering method edit_user of user_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.add_user(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    data = request.json
    user_management_dao.edit_user(data)
    current_app.logger.debug("Exit method add_user of user_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/user/all/', methods=['GET'])
def get_all_urs():
    current_app.logger.debug("Entering method get_user_by of user_management_controller.")
    result = user_management_dao.get_all_urs()
    current_app.logger.debug("Exit method get_user_by of user_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, result)


@blueprint.route('/user/<uid>/', methods=['GET'])
def get_usr_by(uid):
    current_app.logger.debug("Entering method get_user_by of user_management_controller.")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, "uid cannot be empty")
    result = user_management_dao.get_usr_by(uid)
    current_app.logger.debug("Exit method get_user_by of user_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, result)


@blueprint.route('/reset/password/', methods=["POST"])
def reset_password():
    current_app.logger.debug("Entering method reset_password of user_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.reset_password(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    data = request.json
    user_management_dao.reset_password(data)
    current_app.logger.debug("Exit method reset_password of user_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)
