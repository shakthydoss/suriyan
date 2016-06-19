from flask import Flask, Blueprint, jsonify, request, current_app

def update_responce(user_id,tpid,data):
	current_app.logger.debug("Entering method post_tp of user_validator.")
	error = None
	is_valid = True
	if not (data):
		error = "Invalid data"
		is_valid = False	
	if not (data['question_no']):
		error = "Invalid question no"
		is_valid = False
	if not (data['answered']):
		error = "Invalid answered"
		is_valid = False
	current_app.logger.debug("Exit method post_tp of user_validator.")
	return is_valid, error
