import rest.dao.role_management_dao as role_management_dao
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.role_management_validator as validator
from flask import Blueprint, request, current_app

blueprint = Blueprint('role_management_controller', __name__)


@blueprint.route('/role/add/', methods=["POST"])
def add_role():
    current_app.logger.debug("Entering method add_role of role_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.add_role(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    data = request.json
    role_id = role_management_dao.add_role(data)
    return_data = {"role_id": role_id}
    current_app.logger.debug("Exit method add_role of role_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, return_data)


@blueprint.route('/role/edit/', methods=["POST"])
def edit_role():
    current_app.logger.debug("Entering method edit_role of role_management_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.edit_role(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, http_status_codes.MESSAGE_INVALID_INPUTS)
    data = request.json
    role_management_dao.edit_role(data)
    current_app.logger.debug("Exit method edit_role of role_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/role/all/', methods=['GET'])
def get_all_roles():
    current_app.logger.debug("Entering method get_all_roles of role_management_controller.")
    result = role_management_dao.get_all_roles()
    current_app.logger.debug("Exit method get_all_roles of role_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, result)


@blueprint.route('/role/<role_id>/', methods=['GET'])
def get_role_by_id(role_id):
    current_app.logger.debug("Entering method get_role_by_id of role_management_controller.")
    if not role_id:
        return util.to_json(http_status_codes.BAD_REQUEST, "role_id cannot be empty")
    result = role_management_dao.get_role_by_id(role_id)
    current_app.logger.debug("Exit method get_role_by_id of role_management_controller.")
    return util.to_json(http_status_codes.SUCCESS, result)
