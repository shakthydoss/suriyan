
from flask import Flask, jsonify, Blueprint

blueprint = Blueprint('search_controller', __name__)

@blueprint.route('/search', methods=['GET'])
def index():
    return jsonify({'message': 'search request'})
