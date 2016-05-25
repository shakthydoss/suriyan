
from flask import Flask, jsonify, Blueprint
import rest.utils.http_status_codes as status_code

#blueprint object for home controller
blueprint = Blueprint('home_controller', __name__)

@blueprint.route('/', methods=['GET'])
def index():
	print(status_code.SUCCESS)
	return jsonify({'message': 'welcome to otac rest API 1.0. This is display help content'})

@blueprint.route('/help', methods=['GET'])
def help():
	print(status_code.SUCCESS)
	return jsonify({'message': 'welcome to otac rest API 1.0. This is display help content'})
