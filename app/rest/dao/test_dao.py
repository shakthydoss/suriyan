import json

import rest.dao.mongodb as connection_manager_mongo
import rest.utils.util as util
from bson.json_util import dumps
from flask import current_app


def my_testpaper(uid):
    current_app.logger.debug("Entering method test_started of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"uid": uid}
    sort_by = [("invited_on", -1)]
    result = json.loads(dumps(db.tp_usr.find(fltr).sort(sort_by)))
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method test_started of test_dao.")
    return result;


def get_summary_test(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    test = json.loads(dumps(db.tp_usr.find_one(fltr)))
    fltr = {"tpid": tpid}
    tp = json.loads(dumps(db.tp.find_one(fltr)))
    result = dict()
    result["tp"] = tp
    result["test"] = test
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method test_started of test_dao.")
    return result;


def test_started(tpid, uid):
    current_app.logger.debug("Entering method test_started of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    data = {"$set": {"status": "pending"}}
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
    data = {
        "$set": {
            "questions." + data["qid"] + ".response": data["response"],
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
    data = {"$set": {"status": "completed",
                     "completed_on": util.get_unixtime()
                     }}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method test_completed of test_dao.")
    return 1;


def evaluate_result(tpid, uid):
    current_app.logger.debug("Entering method test_completed of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    mark = 0
    negative_mark = 0
    fltr = {"tpid": tpid, "uid": uid}
    test_attempt = db.tp_usr.find_one(fltr)
    for qid in test_attempt["questions"]:
        question = test_attempt["questions"][qid]
        m, nm = compute_mark(question)
        mark = mark + m
        test_attempt["questions"][qid]["mark_obtained"] = str(m)
        negative_mark = negative_mark + nm
    score = mark - negative_mark
    fltr = {'tpid': tpid, "uid": uid, }
    data = {
        "$set": {
            "score": score,
            "questions": test_attempt["questions"]
        }
    }
    result = db.tp_usr.update_one(fltr, data)
    current_app.logger.debug("Exiting method test_completed of test_dao.")
    return 1;


def compute_mark(question):
    mark = 0
    negative_mark = 0
    if question["type"] == "single_choice":
        mark, negative_mark = compute_mark_for_single_choice(question)
    if question["type"] == "multi_choice":
        mark, negative_mark = compute_mark_for_multiple_choice(question)
    if question["type"] == "true_or_false":
        mark, negative_mark = compute_mark_for_true_or_false(question)
    if question["type"] == "fill_up":
        mark, negative_mark = compute_mark_for_fill_in_blank(question)
    if question["type"] == "match":
        mark, negative_mark = compute_mark_for_match(question)
    return mark, negative_mark


def compute_mark_for_single_choice(question):
    mark = 0
    negative_mark = 0
    if question["response"] in question["answers"]:
        mark = int(question["mark_per_correct_answer"])
    else:
        negative_mark = int(question["mark_per_wrong_answer"])
    return mark, negative_mark


def compute_mark_for_multiple_choice(question):
    mark = 0
    negative_mark = 0
    response = question["response"]
    if len(response) > len(question["answers"]):
        response = response[0:len(question["answers"])]
    for ans in response:
        if ans in question["answers"]:
            mark = mark + int(question["mark_per_correct_answer"])
        else:
            negative_mark = negative_mark + int(question["mark_per_wrong_answer"])
    return mark, negative_mark


def compute_mark_for_true_or_false(question):
    mark = 0
    negative_mark = 0
    if question["response"] in question["answers"]:
        mark = int(question["mark_per_correct_answer"])
    else:
        negative_mark = int(question["mark_per_wrong_answer"])
    return mark, negative_mark


def compute_mark_for_fill_in_blank(question):
    mark = 0
    negative_mark = 0
    for ans in question["response"]:
        if ans in question["answers"]:
            mark = mark + int(question["mark_per_correct_answer"])
        else:
            negative_mark = negative_mark + int(question["mark_per_wrong_answer"])
    return mark, negative_mark


def compute_mark_for_match(question):
    mark = 0
    negative_mark = 0
    for ans in question["response"]:
        if ans in question["answers"]:
            mark = mark + int(question["mark_per_correct_answer"])
        else:
            negative_mark = negative_mark + int(question["mark_per_wrong_answer"])
    return mark, negative_mark
