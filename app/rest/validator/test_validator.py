from flask import current_app


def update_response(data):
    current_app.logger.debug("Entering method post_tp of user_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "access_token field is missing"
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'updated_by' in data:
        error = "updated_by field is missing"
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "uid field is missing"
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty"
            is_valid = False
    if not 'tpid' in data:
        error = "tpid field is missing"
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty"
            is_valid = False
    if not 'qid' in data:
        error = "qid field is missing"
        is_valid = False
    if 'qid' in data:
        if not data['qid']:
            error = "qid cannot be empty"
            is_valid = False
    if not 'response' in data:
        error = "response field is missing"
        is_valid = False
    current_app.logger.debug("Exit method post_tp of user_validator.")
    return is_valid, error


def remove_response(data):
    current_app.logger.debug("Entering method remove_response of user_validator.")
    error = None
    is_valid = True
    if not 'access_token' in data:
        error = "access_token field is missing"
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty"
            is_valid = False
    if not 'updated_by' in data:
        error = "updated_by field is missing"
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty"
            is_valid = False
    if not 'uid' in data:
        error = "uid field is missing"
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty"
            is_valid = False
    if not 'tpid' in data:
        error = "tpid field is missing"
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty"
            is_valid = False
    if not 'qid' in data:
        error = "qid field is missing"
        is_valid = False
    if 'qid' in data:
        if not data['qid']:
            error = "qid cannot be empty"
            is_valid = False
    if not 'answer' in data:
        error = "answer field is missing"
        is_valid = False
    if 'answer' in data:
        if not data['answer']:
            error = "answer cannot be empty"
            is_valid = False
    current_app.logger.debug("Exit method post_tp of remove_response.")
    return is_valid, error
