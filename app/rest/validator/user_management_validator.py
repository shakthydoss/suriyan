from flask import current_app


def add_user(data):
    current_app.logger.debug("Entering method add_user of user_management_validator.")
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
    if not 'username' in data:
        error = "Field username is missing."
        is_valid = False
    if 'username' in data:
        if not data['username']:
            error = "username cannot be empty."
            is_valid = False
    if not 'tags' in data:
        error = "Field tags is missing."
        is_valid = False
    if 'tags' in data:
        print(len(data['tags']))
        if len(data['tags']) == 0:
            error = "tags cannot be empty."
            is_valid = False
    if not 'password' in data:
        error = 'Field password id missing.'
        is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
        if not (data['password'].isalnum()):
            error = "Password should be alpha numeric. No special symbols allowed."
            is_valid = False
        if len(data['password']) < 6:
            error = "Minimum of 6 and Max of 12 charater is required for password."
            is_valid = False
        if len(data['password']) > 12:
            error = "Minimum of 6 and Max of 12 charater is required for password."
            is_valid = False
    current_app.logger.debug("Exit method add_user of user_management_validator.")
    return is_valid, error


def edit_user(data):
    current_app.logger.debug("Entering method edit_user of user_management_validator.")
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
    if not 'username' in data:
        error = "Field username is missing."
        is_valid = False
    if 'username' in data:
        if not data['username']:
            error = "username cannot be empty."
            is_valid = False
    if not 'tags' in data:
        error = "Field tags is missing."
        is_valid = False
    if 'tags' in data:
        print(len(data['tags']))
        if len(data['tags']) == 0:
            error = "tags cannot be empty."
            is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    if not 'uid' in data:
        error = 'Field uid id missing.'
        is_valid = False
    current_app.logger.debug("Exit method edit_user of user_management_validator.")
    return is_valid, error


def reset_password(data):
    current_app.logger.debug("Entering method reset_password of user_management_validator.")
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
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    if not 'uid' in data:
        error = 'Field uid id missing.'
        is_valid = False
    if not 'password' in data:
        error = "Field password is missing."
        is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
        if not (data['password'].isalnum()):
            error = "Password should be alpha numeric. No special symbols allowed."
            is_valid = False
        if len(data['password']) < 6:
            error = "Minimum of 6 and Max of 12 charater is required for password."
            is_valid = False
        if len(data['password']) > 12:
            error = "Minimum of 6 and Max of 12 charater is required for password."
            is_valid = False
    current_app.logger.debug("Exit method reset_password of user_management_validator.")
    return is_valid, error
