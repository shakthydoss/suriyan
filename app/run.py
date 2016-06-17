from flask import Flask
import rest.controller.home_controller as home_controller
import rest.controller.search_controller as search_controller
import rest.controller.user_controller as user_controller
import rest.controller.user_management_controller as user_management_controller
import rest.controller.test_paper_controller as test_paper_controller
import rest.controller.auth_controller as auth_controller
import rest.controller.error_handler as error_handler


#creating flask object
app = Flask(__name__)
app.secret_key = 'my_app_secret_key'

#registering blueprint objects to flask 
app.register_blueprint(home_controller.blueprint, url_prefix='/rest')
app.register_blueprint(search_controller.blueprint, url_prefix='/rest')
app.register_blueprint(user_controller.blueprint, url_prefix='/rest')
app.register_blueprint(user_management_controller.blueprint, url_prefix='/rest')
app.register_blueprint(test_paper_controller.blueprint, url_prefix='/rest')
app.register_blueprint(auth_controller.blueprint, url_prefix='/rest')
#app.register_blueprint(error_handler.blueprint, url_prefix='/rest')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
