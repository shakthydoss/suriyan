from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as status_code

#blueprint object for home controller
blueprint = Blueprint('user_management_controller', __name__)

#method to add new user to system.
@blueprint.route('/user/add/', methods=['GET'])
def add_user():
	return jsonify({'message': 'This method will add new user to system'})

#method to add or edit role to user.
@blueprint.route('/user/role/', methods=['GET'])
def add_edit_role(username):
	return jsonify({'message': 'This method will assign or edit role'})

#method to remove user from system.
@blueprint.route('/user/delete/', methods=['GET'])
def edit():
	return jsonify({'message': 'This method will remove  user from system'})