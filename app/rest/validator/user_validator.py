from flask import Flask, Blueprint, jsonify, request, current_app
import re


def change_password(data):
    current_app.logger.debug("Entering method change_password of user_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "access_token field is missing"
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "uid field is missing"
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty"
            is_valid = False
    if not 'secret' in data:
        error = "Password field is missing"
        is_valid = False
    if 'secret' in data:
        if not data['secret']:
            error = "Password field cannot be empty"
            is_valid = False
    if not 'repeat' in data:
        error = "repeat field is missing"
        is_valid = False
    if 'repeat' in data:
        if not data['repeat']:
            error = "repeat field cannot be empty"
            is_valid = False
    if 'secret' in data:
        if not (data['secret'].isalnum()):
            error = "Password should be alpha numeric. No special symbols allowed."
            is_valid = False
        if len(data['secret']) < 6:
            error = "Minimum of 6 and Max of 12 charater is allowed for password."
            is_valid = False
        if len(data['secret']) > 12:
            error = "Minimum of 6 and Max of 12 charater is allowed for password."
            is_valid = False
    if 'repeat' in data and 'secret' in data:
        if data['repeat'] != data['secret']:
            error = "new password and repeat value doest not match"
            is_valid = False
    current_app.logger.debug("Exit method change_password of user_validator.")
    return is_valid, error


def change_username(data):
    current_app.logger.debug("Entering method change_username of user_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "access_token field is missing"
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "uid field is missing"
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty"
            is_valid = False
    if not 'new_username' in data:
        error = "new_username field is missing"
        is_valid = False
    if 'new_username' in data:
        if not data['new_username']:
            error = "new_username cannot be empty"
            is_valid = False
    current_app.logger.debug("Exit method change_username of user_validator.")
    return is_valid, error


def update_my_profile(data):
    current_app.logger.debug("Entering method of update_my_profile of user_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "access_token field is missing"
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "uid field is missing"
        is_valid = False
    if not 'full_name' in data:
        error = "full name field is missing"
        is_valid = False
    if 'full_name' in data:
        if not data['full_name']:
            error = "full name field cannot be empty"
            is_valid = False
    if not 'email' in data:
        error = "email field is missing"
        is_valid = False
    if 'email' in data:
        if not data['email']:
            error = "email field cannot be empty"
            is_valid = False
    if not 'mobile' in data:
        error = "email field is missing"
        is_valid = False
    if 'mobile' in data:
        if not data['mobile']:
            error = "mobile field cannot be empty."
            is_valid = False
        if not data['mobile'].isdigit():
            error = "Not a valid mobile number."
            is_valid = False
    current_app.logger.debug("Exit method of update_my_profile of user_validator.")
    return is_valid, error
