from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as status_code

blueprint = Blueprint('search_controller', __name__)


@blueprint.route('/search', methods=['GET'])
def index():
    return jsonify({'message': 'search request'})
