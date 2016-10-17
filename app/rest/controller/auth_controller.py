from flask import Flask, Blueprint, jsonify, request, current_app, session
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.auth_validator as validator
import rest.dao.auth_dao as auth_dao
import json

blueprint = Blueprint('auth_controller', __name__)


@blueprint.route('/authenticate/', methods=['POST'])
def authenticate():
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.authenticate(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    return_data = auth_dao.authenticate(data)
    return_data = json.loads(return_data)
    return util.to_json(return_data["status"], return_data["data"])


@blueprint.route('/logout/', methods=['POST'])
def logout():
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.logout(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    return_data = auth_dao.logout(data)
    return_data = json.loads(return_data)
    return util.to_json(return_data["status"], return_data["data"])


@blueprint.route('/authenticateToken/', methods=['POST'])
def authenticate_token():
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.authenticate_token(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    return_data = auth_dao.authenticate_token(data)
    return_data = json.loads(return_data)
    return util.to_json(return_data["status"], return_data["data"])
