from flask import current_app


def post_tp(data):
    current_app.logger.debug("Entering method post_tp of test_paper_validator.")
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
    if not 'status' in data:
        error = "Field status is missing."
        is_valid = False
    if 'status' in data:
        if not data['status']:
            error = "status cannot be empty."
            is_valid = False
    if not 'is_active' in data:
        error = "Field is_active is missing."
        is_valid = False
    if 'is_active' in data:
        if not data['is_active']:
            error = "is_active cannot be empty."
            is_valid = False
    if not ('is_active' in data):
        error = "Invalid field is_active"
        is_valid = False
    if ('data' in data):
        for ques in data['data']:
            if not ('sno' in ques):
                error = "Invalid sno"
                is_valid = False
            is_valid, error = validate_question_type(ques)
    current_app.logger.debug("Exit method post_tp of test_paper_validator.")
    return is_valid, error


def validate_question_type(ques):
    error = None
    is_valid = True
    if 'type' not in ques:
        error = "Field type is missing."
        is_valid = False
    if 'type' in ques:
        if not ques['type']:
            error = "type cannot be empty."
            is_valid = False
            return is_valid, error
    if ques['type'] == 'single_choice':
        is_valid, error = validate_single_choice(ques)
        if not (is_valid):
            return is_valid, error
    if ques['type'] == 'multi_choice':
        is_valid, error = validate_multiple_choice(ques)
        if not (is_valid):
            return is_valid, error
    if ques['type'] == 'fill_up':
        is_valid, error = validate_fill_in_blank(ques)
        if not (is_valid):
            return is_valid, error
    if ques['type'] == 'match':
        is_valid, error = validate_match(ques)
        if not (is_valid):
            return is_valid, error
    if ques['type'] == 'true_or_false':
        is_valid, error = validate_true_or_false(ques)
        if not (is_valid):
            return is_valid, error
    return is_valid, error


def validate_single_choice(ques):
    error = None
    is_valid = True
    if not 'options' in ques:
        error = "Field options is missing."
        is_valid = False
    if 'options' in ques:
        if not (len(ques['options']) > 1):
            error = "options cannot be empty."
            is_valid = False
    if not 'answers' in ques:
        error = "Field answers is missing."
        is_valid = False
    if 'answers' in ques:
        print(len(ques['answers']))
        if len(ques['answers']) != 1:
            error = "answers cannot be empty and should be single choice value"
            is_valid = False
    if 'options' in ques and 'answers' in ques:
        for ans in ques['answers']:
            if ans not in ques['options']:
                error = "answers do not match with options specified."
                is_valid = False
    return is_valid, error


def validate_multiple_choice(ques):
    error = None
    is_valid = True
    if not 'options' in ques:
        error = "Field options is missing."
        is_valid = False
    if 'options' in ques:
        if not (len(ques['options']) > 1):
            error = "options cannot be empty."
            is_valid = False
    if not 'answers' in ques:
        error = "Field answers is missing."
        is_valid = False
    if 'answers' in ques:
        if not len(ques['answers']) > 1:
            error = "answers cannot be empty and should be multiple choice."
            is_valid = False
    if 'options' in ques and 'answers' in ques:
        if not len(ques['answers']) <= len(ques['options']):
            error = "Invalid answers"
            is_valid = False
    if 'options' in ques and 'answers' in ques:
        for ans in ques['answers']:
            if ans not in ques['options']:
                error = "answers do not match with options specified."
                is_valid = False
    return is_valid, error


def validate_fill_in_blank(ques):
    error = None
    is_valid = True
    if not ('answers' in ques):
        error = "Field answers is missing"
        is_valid = False
    if 'answers' in ques:
        total_mark_for_this_question = int(ques["total_mark_for_this_question"])
        mark_per_correct_answer = int(ques["mark_per_correct_answer"])
        no_of_fill_up = int(total_mark_for_this_question / mark_per_correct_answer)
        if not (len(ques['answers']) != no_of_fill_up):
            error = "Invalid answers or not all blank has be filled"
            is_valid = False
    return is_valid, error


def validate_match(ques):
    error = None
    is_valid = True
    if not 'left' in ques:
        error = "Field left is missing."
        is_valid = False
    if 'left' in ques:
        if not (len(ques['left']) > 1):
            error = "left side should have more than one value."
            is_valid = False
    if not 'right' in ques:
        error = "Field right is missing."
        is_valid = False
    if 'right' in ques:
        if not (len(ques['right']) > 1):
            error = "right side should have more than one value."
            is_valid = False
    if 'right' in ques and 'left' in ques:
        if not len(ques["right"]) == len(ques["left"]):
            error = "right and left length side should be equal."
            is_valid = False
    if not 'answers' in ques:
        error = "Field answers is missing."
        is_valid = False
    if 'answers' in ques:
        if not (len(ques['answers']) == len(ques["right"])):
            error = "answers length is not matching L.H.S or R.H.S"
            is_valid = False
    return is_valid, error


def validate_true_or_false(ques):
    error = None
    is_valid = True
    if 'answers' not in ques:
        error = "Field answers is missing."
        is_valid = False
    if 'answers' in ques:
        if not ques['answers']:
            error = "answers cannot be empty."
            is_valid = False
    return is_valid, error


def create_tp(data):
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'name' not in data:
        error = "Field name is missing."
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "name cannot be empty."
            is_valid = False
    if 'time_limit' not in data:
        error = "Field time_limit is missing."
        is_valid = False
    if 'time_limit' in data:
        if not data['time_limit']:
            error = "time_limit cannot be empty."
            is_valid = False
    return is_valid, error


def save_or_update(data):
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'name' not in data:
        error = "Field name is missing."
        is_valid = False
    if 'name' in data:
        if not data['name']:
            error = "name cannot be empty."
            is_valid = False
    if 'time_limit' not in data:
        error = "Field time_limit is missing."
        is_valid = False
    if 'time_limit' in data:
        if not data['time_limit']:
            error = "time_limit cannot be empty."
            is_valid = False
    if 'status' not in data:
        error = "Field status is missing."
        is_valid = False
    if 'status' in data:
        if not data['status']:
            error = "status cannot be empty."
            is_valid = False
    return is_valid, error


def add_question_to_tp(data):
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_validator.")
    is_valid, error = check_common_fields_in_question(data)
    if not (is_valid):
        return is_valid, error
    is_valid, error = validate_question_type(data)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_validator.")
    return is_valid, error


def remove_question_from_tp(data):
    current_app.logger.debug("Entering method remove_question_from_tp of test_paper_validator.")
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'tpid' not in data:
        error = "Field tpid is missing."
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty."
            is_valid = False
    if 'qid' not in data:
        error = "Field qid is missing."
        is_valid = False
    if 'qid' in data:
        if not data['qid']:
            error = "qid cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method remove_question_from_tp of test_paper_validator.")
    return is_valid, error


def update_question_to_tp(data):
    current_app.logger.debug("Entering method update_question_to_tp of test_paper_validator.")
    is_valid, error = check_common_fields_in_question(data)
    if not (is_valid):
        return is_valid, error
    is_valid, error = validate_question_type(data)
    current_app.logger.debug("Exiting method update_question_to_tp of test_paper_validator.")
    return is_valid, error


def check_common_fields_in_question(data):
    current_app.logger.debug("Entering method check_common_fields_in_question of test_paper_validator.")
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'tpid' not in data:
        error = "Field tpid is missing."
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty."
            is_valid = False
    if 'qid' not in data:
        error = "Field qid is missing."
        is_valid = False
    if 'qid' in data:
        if not data['qid']:
            error = "qid cannot be empty."
            is_valid = False
    if 'question' not in data:
        error = "Field question is missing."
        is_valid = False
    if 'question' in data:
        if not data['question']:
            error = "question cannot be empty."
            is_valid = False
    if 'type' not in data:
        error = "Field type is missing."
        is_valid = False
    if 'type' in data:
        if not data['type']:
            error = "type cannot be empty."
            is_valid = False
    if 'mark_per_correct_answer' not in data:
        error = "Field mark_per_correct_answer is missing."
        is_valid = False
    if 'mark_per_correct_answer' in data:
        if not data['mark_per_correct_answer']:
            error = "mark_per_correct_answer cannot be empty."
            is_valid = False
    if 'mark_per_wrong_answer' not in data:
        error = "Field mark_per_wrong_answer is missing."
        is_valid = False
    if 'mark_per_wrong_answer' in data:
        if not data['mark_per_wrong_answer']:
            error = "mark_per_wrong_answer cannot be empty."
            is_valid = False
    if 'total_mark_for_this_question' not in data:
        error = "Field total_mark_for_this_question is missing."
        is_valid = False
    if 'total_mark_for_this_question' in data:
        if not data['total_mark_for_this_question']:
            error = "total_mark_for_this_question cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method check_common_fields_in_question of test_paper_validator.")
    return is_valid, error


def update_tags(data):
    current_app.logger.debug("Entering method update_tags of test_paper_validator.")
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'tpid' not in data:
        error = "Field tpid is missing."
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty."
            is_valid = False
    if 'tags' not in data:
        error = "Field tags is missing."
        is_valid = False
    current_app.logger.debug("Exiting method check_common_fields_in_question of test_paper_validator.")
    return is_valid, error


def update_status(data):
    current_app.logger.debug("Entering method update_status of test_paper_validator.")
    error = None
    is_valid = True
    if 'access_token' not in data:
        error = "Field access_token is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'updated_by' not in data:
        error = "Field updated_by is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if 'tpid' not in data:
        error = "Field tpid is missing."
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty."
            is_valid = False
    if 'status' not in data:
        error = "Field status is missing."
        is_valid = False
    if 'status' in data:
        if not data['status']:
            error = "status cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method update_status of test_paper_validator.")
    return is_valid, error


def invite_user_for_test(data):
    current_app.logger.debug("Entering method invite_user_for_test of test_paper_validator.")
    error = None
    is_valid = True
    if 'tpid' not in data:
        error = "Field tpid is missing."
        is_valid = False
    if 'tpid' in data:
        if not data['tpid']:
            error = "tpid cannot be empty."
            is_valid = False
    if not 'uids' in data:
        error = "Field uids is missing."
        is_valid = False
    if 'uids' in data:
        if (len(data['uids']) < 1):
            error = "uids cannot be empty."
            is_valid = False
    if not 'invited_by' in data:
        error = "Field invited_by is missing."
        is_valid = False
    if 'invited_by' in data:
        if (len(data['invited_by']) < 1):
            error = "invited_by cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method invite_user_for_test of test_paper_validator.")
    return is_valid, error
