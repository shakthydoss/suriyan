from flask import Flask, Blueprint, jsonify, request, current_app

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
		error = "secret field is missing"
		is_valid = False
	if 'secret' in data:
		if not data['secret']:
			error = "secret cannot be empty"
			is_valid = False
	if not 'repeat' in data:
		error = "repeat field is missing"
		is_valid = False
	if 'repeat' in data:
		if not data['repeat']:
			error = "repeat cannot be empty"
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
	if not 'username' in data:
		error = "username field is missing"
		is_valid = False
	if 'username' in data:
		if not data['username']:
			error = "username cannot be empty"
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
	keys = data.keys()
	for key in keys:
		if not data[key]:
			error = key + ' is empty' 
			is_valid = False	
	current_app.logger.debug("Exit method of update_my_profile of user_validator.")
	return is_valid, error