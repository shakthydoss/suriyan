from flask import Flask, Blueprint, jsonify, request, current_app
import rest.utils.http_status_codes as http_status_codes
import rest.utils.util as util
import rest.dao.temp_dao as temp_dao
import rest.validator.temp_validator as validator
import rest.dao.test_paper_dao as test_paper_dao


#blueprint object for home controller
blueprint = Blueprint('user_controller', __name__)

@blueprint.route('/<user_id>/', methods=['GET'])
def dashboard(user_id):
	return jsonify({'message': 'This is dashboard'})

@blueprint.route('/<user_id>/tpid/<tpid>/summary', methods=['GET'])
def summary(user_id, tpid):
	return jsonify({'message':'test paper summary page'})

@blueprint.route('/<user_id>/tpid/<tpid>/started', methods=['POST'])
def started(user_id, tpid):
	current_app.logger.debug("Entering method started of user_controller.")
	temp_dao.started(user_id,tpid)
	current_app.logger.debug("Exit method started of user_controller.")
	status_message = "success"
	return_data = str(_id)
	temp_dao.started(user_id,tpid)
	return util.to_json(status_code, status_message, return_data)

@blueprint.route('/<user_id>/tpid/<tpid>/update_responce', methods=['POST'])
def update_responce(user_id, tpid):
	current_app.logger.debug("Entering method started of user_controller.")
	data = request.json
	is_valid, error = validator.update_responce(user_id,tpid,data)
	if not (is_valid):
		return util.to_json(http_status_codes.BAD_REQUEST, error, None)
	temp_dao.update_responce(user_id,tpid,data)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	return_data = None
	temp_dao.started(user_id,tpid)
	current_app.logger.debug("Exit method started of user_controller.")
	return util.to_json(status_code, status_message, return_data)


# method brings data for review page before submitting
@blueprint.route('/<user_id>/tpid/<tpid>/review', methods=['GET'])
def review(user_id, tpid):
	current_app.logger.debug("Entering method review of user_controller.")
	return_data = temp_dao.review(user_id,tpid)
	status_code = http_status_codes.SUCCESSFULLY_CREATED
	status_message = "success"
	temp_dao.started(user_id,tpid)
	current_app.logger.debug("Exit method review of user_controller.")
	return util.to_json(status_code, status_message, return_data)

# method submits the test paper for evalution
@blueprint.route('/<user_id>/tpid/<tpid>/submit', methods=['GET'])
def submit(user_id, tpid):
	current_app.logger.debug("Entering method submit of user_controller.")
	temp_dao.submit(user_id,tpid)
	evaluate_submission(user_id,tpid)
	current_app.logger.debug("Exit method submit of user_controller.")
	return jsonify({'message':'submit'})

def evaluate_submission(user_id,tpid):
	current_app.logger.debug("Entering method evaluate_submission of user_controller.")
	tp = test_paper_dao.get_tp_by_id(tpid)
	tp_urs = temp_dao.get_responce(user_id, tpid)
	questions = tp['data']
	for question in questions:
		sno = question['sno']
		if tp_urs[str(sno)]:
			if(question['type'] == "single_choice"):
				total_mark, total_negative_mark = case_single_choice_get_marks(question, tp_urs[str(sno)])
			if(question['type'] == "single_choice"):
				total_mark, total_negative_mark = case_multiple_choice_get_marks(question, tp_urs[str(sno)])			
			if(question['type'] == "fill_in_blanks"):
				total_mark, total_negative_mark = case_fill_in_blank_get_marks(question, tp_urs[str(sno)])
			if(question['type'] == "match"):
				total_mark, total_negative_mark = case_match_get_marks(question, tp_urs[str(sno)])
			if(question['type'] == "true_or_false"):
				total_mark, total_negative_mark = case_single_choice_get_marks(question, tp_urs[str(sno)])
			total_mark_obtained =  total_mark - int(round(total_negative_mark))
			data = tp_urs[str(sno)]
			data['total_mark_obtained'] = total_mark_obtained
			temp_dao.update_responce(user_id,tpid,data)
	current_app.logger.debug("Exit method evaluate_submission of user_controller.")
	return "success"

def case_single_choice_get_marks(question, responce):
	total_mark  = 0 		# total mark for correct answer 
	total_negative_mark = 0 # total negative mark 
	if(question['answer'] == responce['answered']):
		total_mark = question['mark_per_correct_answer']
	else:
		total_negative_mark = question['mark_per_wrong_answer']
	return int(total_mark), int(total_negative_mark)

def case_multiple_choice_get_marks(question, responce):
	total_mark  = 0 		# total mark for correct answer 
	total_negative_mark = 0 # total negative mark 
	if(set(question['answer']) == set(responce['answered'])):
		total_mark = question['total_mark_for_this_question']
	else:
		# number of correct responce.
		n = len(set(question['answer']).intersection(responce['answered']))
		# number of wrong responce. 
		w = len(question['answer']) - n 
		total_mark = n * int(question['mark_per_correct_answer'])
		total_negative_mark = w * int(question['mark_per_wrong_answer'])
	return int(total_mark), int(total_negative_mark)

def case_fill_in_blank_get_marks(question, responce):
	total_mark  = 0 		# total mark for correct answer 
	total_negative_mark = 0 # total negative mark 
	n = 0					# number of correct responce.
	w = 0					# number of wrong responce.
	if(set(question['answer']) == set(responce['answered'])):
		total_mark = question['total_mark_for_this_question']
	else:
		size = len(question['answer'])
		for index in size:
			if(question['answer'][str(index)] == responce['answered'][str(index)]):
				n = n + 1
			else:
				w = w + 1
		total_mark = n * int(question['mark_per_correct_answer'])
		total_negative_mark = w * int(question['mark_per_wrong_answer'])
	return "success"

def case_match_get_marks(question, responce):
	total_mark  = 0 		# total mark for correct answer 
	total_negative_mark = 0 # total negative mark 
	if(set(question['answer']) == set(responce['answered'])):
		total_mark = question['total_mark_for_this_question']
	else:
		# number of correct responce.
		n = len(set(question['answer']).intersection(responce['answered']))
		# number of wrong responce. 
		w = len(question['answer']) - n 
		total_mark = n * int(question['mark_per_correct_answer'])
		total_negative_mark = w * int(question['mark_per_wrong_answer'])
	return int(total_mark), int(total_negative_mark)