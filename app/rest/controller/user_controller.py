from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as status_code

#blueprint object for home controller
blueprint = Blueprint('user_controller', __name__)

#method brings data to user dashboard
@blueprint.route('/<username>/', methods=['GET'])
def dashboard(username):
	return jsonify({'message': 'This is dashboard'})

# method for test paper summary page.
@blueprint.route('/<username>/tpid/<tpid>/summary', methods=['GET'])
def summary(username, tpid):
	return jsonify({'message':'test paper summary page'})

# method retrives all questions and options to the test paper. 
@blueprint.route('/<username>/tpid/<tpid>/get', methods=['GET'])
def get(username, tpid):
	return jsonify({'message':'retrives all questions'})

# method updates, test assessment has been started to server.
@blueprint.route('/<username>/tpid/<tpid>/started', methods=['GET'])
def started(username, tpid):
	return jsonify({'message':'started'})

# method brings data for review page before submitting
@blueprint.route('/<username>/tpid/<tpid>/review', methods=['GET'])
def review(username, tpid):
	return jsonify({'message':'review'})

# method submits the test paper
@blueprint.route('/<username>/tpid/<tpid>/submit', methods=['GET'])
def submit(username, tpid):
	return jsonify({'message':'submit'})

# method submits the test paper
@blueprint.route('/<username>/edit/profile', methods=['GET'])
def edit_profile():
	return jsonify({'message':'method to edit user personal details'})

