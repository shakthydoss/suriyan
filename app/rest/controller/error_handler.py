from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as status_code
import rest.utils.util as util

#blueprint object for home controller
blueprint = Blueprint('error_handler', __name__)

@blueprint.app_errorhandler(404)
def page_not_found(error):
	current_app.logger.error('resource not found: %s', (request.path))
	return util.to_json(400, None), 400 

@blueprint.app_errorhandler(500)
def internal_server_error(error):
	current_app.logger.error('server error: %s', (error))
	return util.to_json(500, None), 500 

@blueprint.app_errorhandler(Exception)
def unhandled_exception(error):
	current_app.logger.error('unhandled exception: %s', (error))
	return util.to_json(500, None), 500