from flask import current_app


def add_role(data):
    current_app.logger.debug("Entering method add_role of role_management_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if not 'updated_by' in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if not 'name' in data:
        error = "Field name is missing."
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "name cannot be empty."
            is_valid = False
    if not 'permissions' in data:
        error = "Field permissions is missing."
        is_valid = False
    if 'permissions' in data:
        print(len(data['permissions']))
        if len(data['permissions']) == 0:
            error = "permissions cannot be empty."
            is_valid = False
    current_app.logger.debug("Exit method add_role of role_management_validator.")
    return is_valid, error


def edit_role(data):
    current_app.logger.debug("Entering method add_role of role_management_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if not 'updated_by' in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if not 'role_id' in data:
        error = "Field role_id is missing."
        is_valid = False
    if 'role_id' in data:
        if not data['role_id']:
            error = "role_id cannot be empty."
            is_valid = False
    if not 'name' in data:
        error = "Field name is missing."
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "name cannot be empty."
            is_valid = False
    if not 'permissions' in data:
        error = "Field permissions is missing."
        is_valid = False
    if 'permissions' in data:
        print(len(data['permissions']))
        if len(data['permissions']) == 0:
            error = "permissions cannot be empty."
            is_valid = False
    current_app.logger.debug("Exit method add_role of role_management_validator.")
    return is_valid, error
