from flask import current_app


def save_tag(data):
    current_app.logger.debug("Entering method save_tag of tag_validator.")
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
    if not 'name' in data:
        error = "Tag name field is missing"
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "Tag name cannot be empty"
            is_valid = False
    if not 'description' in data:
        error = "Tag description field is missing"
        is_valid = False
    if 'description' in data:
        if not data['description']:
            error = "Tag description cannot be empty"
            is_valid = False
    current_app.logger.debug("Exit method save_tag of tag_validator.")
    return is_valid, error


def update_tag(data):
    current_app.logger.debug("Entering method update_tag of tag_validator.")
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
    if not 'name' in data:
        error = "Tag name field is missing"
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "Tag name cannot be empty"
            is_valid = False
    if not 'description' in data:
        error = "Tag description field is missing"
        is_valid = False
    if 'description' in data:
        if not data['description']:
            error = "Tag description cannot be empty"
            is_valid = False
    if not 'tag_id' in data:
        error = "Tag id field is missing"
        is_valid = False
    if 'tag_id' in data:
        if not data['tag_id']:
            error = "Tag id cannot be empty"
            is_valid = False
    current_app.logger.debug("Exit method update_tag of tag_validator.")
    return is_valid, error
