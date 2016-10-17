from flask import current_app
import rest.dao.mongodb as connection_manager_mongo
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util
from bson.objectid import ObjectId
from bson.json_util import dumps


def get_tp_by_id(tpid):
    current_app.logger.debug("Entering method get_tp_by_id of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp.find_one({"_id": ObjectId(tpid)})
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


def invite_user_for_test(tpid, uid):
    current_app.logger.debug("Entering method invite_user_for_test tp of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp_usr.find_one({"tpid":tpid ,"uid": uid})
    print result
    if result is None:
        data = {
            "tpid": tpid,
            "uid": uid,
            "update_on": util.get_current_ts_in_ms(),
            "completed": "n",
            "started": "n"
        }
        result = db.tp_usr.insert_one(data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method invite_user_for_test tp of test_paper_dao.")


def get_tp_by_uid(uid):
    current_app.logger.debug("Entering method invite_user_for_test tp of test_paper_dao.")
    db, connection = connection_manager_mongo.get_connection()
    doc = {
        "$and": [{
            "audit.created_by": "12346"
        },{
            "status": {
                "$ne": "closed"
            }
        }]
    }
    result = dumps(db.tp.find(doc))

    #result['_id'] = str(result['_id'])
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method invite_user_for_test tp of test_paper_dao.")
    return result


def create_tp(data):
    current_app.logger.debug("Entering method create_tp of test_paper_dao.")
    tmp = dict()
    tmp["name"] = data["name"]
    audit = dict()
    current_ts = util.get_current_ts_in_ms()
    audit["created_on"] = current_ts
    audit["updated_on"] = current_ts
    audit["created_by"] = data["updated_by"]
    audit["updated_by"] = data["updated_by"]
    tmp["audit"] = audit
    tmp["status"] = "draft"
    db, connection = connection_manager_mongo.get_connection()
    result = db.tp.insert_one(tmp)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method create_tp of test_paper_dao.")
    return result.inserted_id


def add_question_to_tp(data):
    current_app.logger.debug("Entering method add_question_to_tp of test_paper_dao.")
    del data["access_token"]
    del data["updated_by"]
    tpid = data["tpid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'_id': ObjectId(tpid)}
    data = {
        "$addToSet": {
            "data": data
        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method add_question_to_tp of test_paper_dao.")
    return None


def remove_question_from_tp(data):
    current_app.logger.debug("Entering method remove_question_from_tp of test_paper_dao.")
    del data["access_token"]
    del data["updated_by"]
    tpid = data["tpid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'_id': ObjectId(tpid)}
    data = {
        "$pull": {
            "data": data
        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method remove_question_from_tp of test_paper_dao.")
    return None


def update_question_to_tp(data):
    current_app.logger.debug("Entering method remove_question_from_tp of test_paper_dao.")
    del data["access_token"]
    del data["updated_by"]
    tpid = data["tpid"]
    del data["tpid"]
    db, connection = connection_manager_mongo.get_connection()
    fltr = {'_id': ObjectId(tpid), "data.qid": data["qid"]}
    data = {
        "$set": {
            "data.$.question": data["question"],
            "data.$.mark_per_correct_answer": data["mark_per_correct_answer"],
            "data.$.mark_per_wrong_answer": data["mark_per_wrong_answer"],
            "data.$.total_mark_for_this_question": data["total_mark_for_this_question"],
            "data.$.type": data["type"],
        }
    }
    result = db.tp.update_one(fltr, data)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method remove_question_from_tp of test_paper_dao.")
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
