from flask import Flask, Blueprint, jsonify, request, current_app


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


def add_role(data):
    current_app.logger.debug("Entering method add_role of user_management_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "Field uid is missing"
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty"
            is_valid = False
    if not 'role_ids' in data:
        error = "Field role_ids cannot be empty"
        is_valid = False
    if 'role_ids' in data:
        if not (isinstance(data['role_ids'], list)):
            error = "role_ids should be an array"
            is_valid = False
    current_app.logger.debug("Exit method add_role of user_management_validator.")
    return is_valid, error
