from flask import Flask, jsonify, Blueprint
import rest.utils.http_status_codes as status_code

#blueprint object for home controller
blueprint = Blueprint('test_paper_controller', __name__)

# uploads the test paper and saves as draft
@blueprint.route('/<username>/uploadtp', methods=['GET'])
def uploadtp(username):
	return jsonify({'message': 'uploadtp'})

# method to publish the test paper. 
@blueprint.route('/<username>/tpid/<tpid>/publish', methods=['GET'])
def publish(username,tpid):
	return jsonify({'message': 'uploadtp'})

# maked as inactive.this test paper can not be taken in futher.
@blueprint.route('/<username>/tpid/<tpid>/delete', methods=['GET'])
def delete(username,tpid):
	return jsonify({'message': 'uploadtp'})
