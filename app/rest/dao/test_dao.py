from flask import current_app
import rest.dao.mongodb as connection_manager_mongo
import rest.utils.util as util
import rest.utils.gobal_variable as gobal_variable
import requests
import json
from bson.objectid import ObjectId


def test_started(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    data = {"$set": {"started": "y"}}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method test_started of test_dao.")
    return 1;


def update_response(data):
    current_app.logger.debug("Entering method update_response of test_dao.")
    tpid = data['tpid']
    uid = data['uid']
    del data["access_token"]
    del data["updated_by"]
    del data["uid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()

    fltr = {'tpid': tpid, "uid": uid, }
    response = {
        "qid": data["qid"],
        "answer": data["answer"]
    }
    data = {
        "$set": {
            "data." + data["qid"]: response,
        }
    }
    result = db.tp_usr.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method update_response of test_dao.")
    return 1


def remove_response(data):
    current_app.logger.debug("Entering method remove_response of test_dao.")
    tpid = data['tpid']
    uid = data['uid']
    del data["access_token"]
    del data["updated_by"]
    del data["uid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'tpid': tpid, "uid": uid, }
    data = {
        "$unset": {
            "data." + data["qid"]: 1,
        }
    }
    result = db.tp_usr.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method remove_response of test_dao.")
    return 1


def test_completed(tpid, uid):
    current_app.logger.debug("Entering method test_completed of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    data = {"$set": {"completed": "y"}}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method test_completed of test_dao.")
    return 1;


def evaluate_result(tpid, uid):
    current_app.logger.debug("Entering method test_completed of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    mark = 0
    negative_mark = 0
    t = 0
    fltr = {"_id": ObjectId(tpid)}
    json_questions = db.tp.find_one(fltr)
    fltr = {"tpid": tpid, "uid": uid}
    json_response = db.tp_usr.find_one(fltr)
    for question in json_questions["data"]:
        qid = question["qid"]
        t = t + int(question["total_mark_for_this_question"])
        if qid in json_response["data"]:
            m, n_m = compute_mark(question, json_questions["data"][qid])
            mark = mark + m
            negative_mark = negative_mark + n_m
    score = mark - negative_mark
    fltr = {'tpid': tpid, "uid": uid, }
    data = {
        "$set": {
            "score": score,
            "total_marks": t
        }
    }
    result = db.tp_usr.update_one(fltr, data)
    current_app.logger.debug("Exiting method test_completed of test_dao.")
    return 1;


def compute_mark(question, response):
    mark = 0
    negative_mark = 0
    if question["type"] == "single_choice":
        mark, negative_mark = compute_mark_for_single_choice
    if question["type"] == "multiple_choice":
        mark, negative_mark = compute_mark_for_multiple_choice
    if question["type"] == "true_or_false":
        mark, negative_mark = compute_mark_for_true_or_false
    if question["type"] == "fill_in_blank":
        mark, negative_mark = compute_mark_for_fill_in_blank
    if question["type"] == "match":
        mark, negative_mark = compute_mark_for_match
    return mark, negative_mark


def compute_mark_for_single_choice(question, response):
    mark = 0
    negative_mark = 0
    if response["answer"] in question["answer"]:
        mark = question["mark_per_correct_answer"]
    else:
        negative_mark = question["mark_per_wrong_answer"]
    return mark, negative_mark


def compute_mark_for_multiple_choice(question, response):
    mark = 0
    negative_mark = 0
    for ans in response["answer"]:
        if ans == question["answer"]:
            mark = mark + question["mark_per_correct_answer"]
        else:
            negative_mark = negative_mark + question["mark_per_wrong_answer"]
    return mark, negative_mark


def compute_mark_for_true_or_false(question, response):
    mark = 0
    negative_mark = 0
    if response["answer"] == question["answer"]:
        mark = question["mark_per_correct_answer"]
    else:
        negative_mark = question["mark_per_wrong_answer"]
    return mark, negative_mark


def compute_mark_for_fill_in_blank(question, response):
    mark = 0
    negative_mark = 0
    for ans in response["answer"]:
        if ans == question["answer"]:
            mark = mark + question["mark_per_correct_answer"]
        else:
            negative_mark = negative_mark + question["mark_per_wrong_answer"]
    return mark, negative_mark


def compute_mark_for_match(question, response):
    mark = 0
    negative_mark = 0
    for ans in response["answer"]:
        if ans == question["answer"]:
            mark = mark + question["mark_per_correct_answer"]
        else:
            negative_mark = negative_mark + question["mark_per_wrong_answer"]
    return mark, negative_mark
