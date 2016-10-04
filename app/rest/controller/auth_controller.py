from flask import Flask, Blueprint, jsonify, request, current_app, session
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.auth_validator as validator
import rest.dao.auth_dao as auth_dao

blueprint = Blueprint('auth_controller', __name__)


@blueprint.route('/authenticate/', methods=['POST'])
def authenticate():
    current_app.logger.debug("Entering method authenticate of auth_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.authenticate(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
        # return_value = auth_dao.authenticate(data)
    temp = {}
    temp["access_token"] = "12345678901234567890"
    return util.to_json(http_status_codes.SUCCESS, "return_data")


@blueprint.route('/signout/', methods=['POST'])
def logout():
    current_app.logger.debug("Entering method signout.")
    # TODO
    current_app.logger.debug("Exit method signout.")
    return util.to_json(http_status_codes.SUCCESS, None)
