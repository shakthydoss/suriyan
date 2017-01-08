import rest.dao.auth_dao as auth_dao
import rest.dao.user_dao as user_dao
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.validator.user_validator as validator
from flask import Blueprint, request, current_app

blueprint = Blueprint('user_controller', __name__)


@blueprint.route('/changePassword/', methods=['Post'])
def change_password():
    current_app.logger.debug("Entering method change_password of user_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.change_password(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input')
    data = request.json
    if auth_dao.is_logged_in(data['access_token']) == False:
        return util.to_json(http_status_codes.UNAUTHORIZED, 'Not Authorized')
    return_value = user_dao.change_password(data)
    status_code = None
    status_message = None
    return_data = None
    if return_value == 1:
        status_code = 200
        status_message = "Success"
        return_data = None
    if return_value == -1:
        status_code = 400
        status_message = "Bad Request"
        return_data = None
    current_app.logger.debug("Exit method change_password of user_controller.")
    return util.to_json(status_code, return_data)


@blueprint.route('/changeUsername/', methods=['Post'])
def change_username():
    current_app.logger.debug("Entering method change_username of user_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.change_username(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input')
    data = request.json
    status_code = None
    return_data = None
    return_value = user_dao.change_username(data)
    if return_value == 1:
        status_code = 200
        return_data = "success"
    if return_value == -1:
        status_code = 400
        return_data = data['new_username'] + " is not avaiable. or could't process the request."
    current_app.logger.debug("Exit method change_username of user_controller.")
    return util.to_json(status_code, return_data)


@blueprint.route('/getRole/uid/<uid>/', methods=['GET'])
def get_role_for_user(uid):
    current_app.logger.debug("Entering method get_role_for_user of user_controller.")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, error)
    return_value, list_roles = user_dao.get_role_for_user(uid)
    if return_value == 1:
        status_code = 200
        status_message = "success"
        return_data = {'roles': list_roles}
    if return_value == -1:
        status_code = 400
        status_message = "Bad Request"
        return_data = None
    current_app.logger.debug("Exit method get_role_for_user of user_controller.")
    return util.to_json(status_code, return_data)


@blueprint.route('/updateProfile/', methods=['POST'])
def update_my_profile():
    current_app.logger.debug("Entering method of update_my_profile of user_controller.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_my_profile(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input')
    data = request.json
    # if auth_dao.is_logged_in(data['access_token']) == False:
    #    return util.to_json(http_status_codes.UNAUTHORIZED, 'Not Authorized')
    user_dao.update_my_profile(data)
    return_data = None
    status_code = 200
    status_message = "success"
    current_app.logger.debug("Exit method of update_my_profile of user_controller.")
    return util.to_json(status_code, return_data)


@blueprint.route('/getProfile/uid/<uid>/', methods=['GET'])
def get_my_profile(uid):
    current_app.logger.debug("Entering method of update_my_profile of user_controller.")
    if not uid:
        return util.to_json(http_status_codes.BAD_REQUEST, 'invalid input')
    return_data = user_dao.get_my_profile(uid)
    status_code = 200
    status_message = "success"
    current_app.logger.debug("Exit method of update_my_profile of user_controller.")
    return util.to_json(status_code, return_data)
