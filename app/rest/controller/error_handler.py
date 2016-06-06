from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as status_code

#blueprint object for home controller
blueprint = Blueprint('error_handler', __name__)

@blueprint.app_errorhandler(404)
def page_not_found(error):
	current_app.logger.error('Page not found: %s', (request.path))
	return jsonify({'message': '404'}), 404

@blueprint.app_errorhandler(500)
def internal_server_error(error):
    current_app.logger.error('Server Error: %s', (error))
    return jsonify({'message': '500'}), 500

@blueprint.app_errorhandler(Exception)
def unhandled_exception(error):
    current_app.logger.error('Unhandled Exception: %s', (error))
    return jsonify({'message': '500'}), 500