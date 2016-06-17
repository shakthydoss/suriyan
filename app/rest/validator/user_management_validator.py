from flask import Flask, Blueprint, jsonify, request, current_app

def add_user(data):
	current_app.logger.debug("Entering method add_user of user_management_controller_validator.")
	error = None
	is_valid = True
	if not (data):
		error = "Invalid data"
		is_valid = False
	if not ('name' in data):
		error = "Invalid name"
		is_valid = False
	current_app.logger.debug("Exit method add_user of user_management_controller_validator.")
	return is_valid, error

def add_role(data):
	current_app.logger.debug("Entering method add_role of user_management_controller_validator.")
	error = None
	is_valid = True
	if not (data):
		error = "Invalid data"
		is_valid = False
	if not ('uid' in data):
		error = "Invalid uid"
		is_valid = False
	if not ('role_ids' in data):
		error = "Invalid role ids"
		is_valid = False
	if not (isinstance(data['role_ids'], list)):
		error = "Invalid role ids - should be an array"
		is_valid = False
	current_app.logger.debug("Exit method add_role of user_management_controller_validator.")
	return is_valid, error