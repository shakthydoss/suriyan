import json

import rest.dao.mongodb as connection_manager_mongo
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import current_app


def get_tp_by_id(tpid):
    current_app.logger.debug("Entering method get_tp_by_id of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp.find_one({"tpid": tpid})
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method get_tp_by_id of test_paper_dao.")
    result['_id'] = str(result['_id'])
    return result


def post_tp(data):
    current_app.logger.debug("Entering method add_user of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp.insert_one(data)
    connection_manager_mongo.close_connection(connection)
    try:
        dbmysql = connection_manager_mysql.get_connection()
        cursor = dbmysql.cursor()
        sql = "insert into tp (tpid,name,updated_by) values ( %s,%s,%s);"
        cursor.execute(sql, (str(result.inserted_id), data['name'], data['updated_by'],))
        dbmysql.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        dbmysql.rollback()
    current_app.logger.debug("Exit method add_user of test_paper_dao.")
    return result.inserted_id


def invite_user_for_test(tpid, uid, invited_by):
    current_app.logger.debug("Entering method invite_user_for_test tp of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp_usr.find_one({"tpid": tpid, "uid": uid})
    print result
    if result is None:
        tp = db.tp.find_one({"tpid": tpid})
        questions = tp["questions"]
        for qid in questions:
            questions[qid]["response"] = []
        data = {
            "tpid": tpid,
            "name": tp["name"],
            "uid": uid,
            "invited_on": util.get_unixtime(),
            "invited_by": invited_by,
            "status": "not-started",
            "total_make_for_this_tp": tp["total_make_for_this_tp"],
            "questions": questions
        }
        result = db.tp_usr.insert_one(data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method invite_user_for_test tp of test_paper_dao.")


def get_tp_by_uid(uid):
    current_app.logger.debug("Entering method get_tp_by_uid tp of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    doc = {
        "$and": [{
            "audit.created_by": uid
        }, {
            "status": {
                "$ne": "closed"
            }
        }],
    }
    sort_by = [("audit.updated_on", -1)]
    result = dumps(db.tp.find(doc).sort(sort_by))
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method get_tp_by_uid of test_paper_dao.")
    return result


def create_tp(data):
    current_app.logger.debug("Entering method create_tp of test_paper_dao.")
    tmp = dict()
    tmp["name"] = data["name"]
    tmp["tag"] = data["tag"].split(",")
    tmp["time_limit"] = data["time_limit"]
    tmp["tpid"] = util.get_key()
    audit = dict()
    current_ts = util.get_unixtime()
    audit["created_on"] = current_ts
    audit["updated_on"] = current_ts
    audit["created_by"] = data["updated_by"]
    audit["updated_by"] = data["updated_by"]
    tmp["audit"] = audit
    tmp["status"] = "draft"
    tmp["total_make_for_this_tp"] = -1
    tmp["questions"] = dict()
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp.insert_one(tmp)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method create_tp of test_paper_dao.")
    return tmp["tpid"]


def save_or_update(data):
    current_app.logger.debug("Entering method save_or_update of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'tpid': data["tpid"]}
    total_make_for_this_tp = 0
    result = db.tp.find_one(fltr)
    if data["status"] == "published":
        for question in result["questions"]:
            total_make_for_this_tp = total_make_for_this_tp + int(
                result["questions"][question]["total_mark_for_this_question"])
    data = {
        "$set": {
            "name": data["name"],
            "tag": data["tag"],
            "time_limit": data["time_limit"],
            "status": data["status"],
            "total_make_for_this_tp": total_make_for_this_tp
        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method save_or_update of test_paper_dao.")


def add_question_to_tp(data):
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_dao.")
    del data["access_token"]
    del data["updated_by"]
    tpid = data["tpid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'tpid': tpid}
    print(data)
    data = {
        "$set": {
            "questions." + data["qid"]: data,

        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_dao.")
    return None


def remove_question_from_tp(data):
    current_app.logger.debug("Entering method remove_question_from_tp of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'tpid': data["tpid"]}
    data = {
        "$unset": {
            "questions." + data["qid"]: "-1"
        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method remove_question_from_tp of test_paper_dao.")
    return None


def update_question_to_tp(data):
    current_app.logger.debug("Entering method update_question_to_tp of test_paper_dao.")
    del data["access_token"]
    del data["updated_by"]
    tpid = data["tpid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'tpid': tpid}
    print(data)
    data = {
        "$set": {
            "questions." + data["qid"]: data,

        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method update_question_to_tp of test_paper_dao.")
    return None


def update_tags(data):
    current_app.logger.debug("Entering method update_tags of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'_id': ObjectId(data["tpid"])}
    doc = {
        "$set": {
            "tags": []
        }
    }
    result = db.tp.update_one(fltr, doc)
    print data["tags"]
    doc = {
        "$pushAll": {
            "tags": data["tags"]
        }
    }
    result = db.tp.update_one(fltr, doc)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method update_tags of test_paper_dao.")
    return None


def update_status(data):
    current_app.logger.debug("Entering method update_status of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'_id': ObjectId(data["tpid"])}
    doc = {
        "$set": {
            "status": data["status"]
        }
    }
    result = db.tp.update_one(fltr, doc)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method update_tags of test_paper_dao.")
    return None


def view_report(tpid):
    current_app.logger.debug("Entering method view_report of test_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp_usr.aggregate([
        {
            "$match": {"tpid": tpid, "status": "completed"}
        },
        {
            "$sort": {"completed_on": -1}
        },
        {
            "$lookup": {
                "from": "usr",
                "localField": "uid",
                "foreignField": "uid",
                "as": "usr_detail"
            }
        }
    ])
    result = json.loads(dumps(result))
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method view_report of test_dao.")
    return result;
