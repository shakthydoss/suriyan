from flask import Flask, Blueprint, jsonify, request, current_app


def post_tp(data):
	current_app.logger.debug("Entering method post_tp of test_paper_validator.")
	error = None
	is_valid = True
	if not (data):
		error = "Invalid data"
		is_valid = False
	if not ('name' in data):
		error = "Invalid name"
		is_valid = False
	if not ('data' in data):
		error = "Invalid data"
		is_valid = False
	if ('data' in data):
		for ques in data['data']:
			if not ('sno' in ques):
				error = "Invalid sno"
				is_valid = False
			is_valid, error = validate_question(ques)
	current_app.logger.debug("Exit method post_tp of test_paper_validator.")
	return is_valid, error

def validate_question(ques):
	error = None
	is_valid = True
	if not ('type' in ques):
		error = "Invalid question type"
		is_valid = False
	if ('type' in ques):
		if (ques['type'] == 'single_choice'):
			is_valid, error = case_single_choice(ques) 
			if not (is_valid):
				return is_valid, error
		if (ques['type'] == 'multiple_choice'):
			is_valid, error = case_multiple_choice(ques) 
			if not (is_valid):
				return is_valid, error
		if (ques['type'] == 'fill_in_blanks'):
			is_valid, error = case_fill_in_blank(ques) 
			if not (is_valid):
				return is_valid, error
		if (ques['type'] == 'match'):
			is_valid, error = case_match(ques) 
			if not (is_valid):
				return is_valid, error
	return is_valid, error


def case_single_choice(ques):
	error = None
	is_valid = True
	if not ('option' in ques):
		error = "Invalid option - single question question"
		is_valid = False
	if ('option' in ques):
		if not (len(ques['option']) > 1):
			error = "Invalid option - single question question"
			is_valid = False
	if not ('answer' in ques):
		error = "Invalid answer - single question question"
		is_valid = False
	if ('answer' in ques):
		if not (len(ques['answer']) == 1):
			error = "answer answer - single question question"
			is_valid = False
	return is_valid, error

def case_multiple_choice(ques):
	error = None
	is_valid = True
	if not ('option' in ques):
		error = "Invalid option - multiple choice question"
		is_valid = False
	if ('option' in ques):
		if not (len(ques['option']) > 1):
			error = "Invalid option - multiple choice question"
			is_valid = False
	if not ('answer' in ques):
		error = "Invalid answer - multiple choice question"
		is_valid = False
	if ('answer' in ques):
		if not (len(ques['answer']) > 1):
			error = "answer answer - multiple choice question"
			is_valid = False
	return is_valid, error

def case_fill_in_blank(ques):
	error = None
	is_valid = True
	if not ('answer' in ques):
		error = "Invalid answer - fil in blank"
		is_valid = False
	if ('answer' in ques):
		if not (len(ques['answer']) >= 1 ):
			error = "Invalid answer - fil in blank"
			is_valid = False
	return is_valid, error

def case_match(ques):
	error = None
	is_valid = True
	if not ('left' in ques):
		error = "Invalid left"
		is_valid = False
	if not ('right' in ques):
		error = "Invalid right"
		is_valid = False
	return is_valid, error


