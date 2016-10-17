from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.user_management_validator as validator
import rest.dao.user_management_dao as user_management_dao
import rest.dao.auth_dao as auth_dao
import json

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
    return_data = user_management_dao.add_user(data)
    return_data = json.loads(return_data)
    current_app.logger.debug("Exit method add_user of user_management_controller.")
    return util.to_json(return_data["status"], return_data["data"])


@blueprint.route('/user/role/', methods=["POST"])
def add_role():
    current_app.logger.debug("Entering method add_role of user_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.add_role(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    data = request.json
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
    return util.to_json(status_code, return_data)
