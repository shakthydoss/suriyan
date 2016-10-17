from flask import current_app
import rest.dao.mongodb as connection_manager
import rest.utils.util as util


def started(uid, tpid):
    current_app.logger.debug("Entering method started of user_dao.")
    db, connection = connection_manager.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    data = {"$set": {"started": "y"}}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager.close_connection(connection)
    current_app.logger.debug("Exit method started of user_dao.")


def completed(uid, tpid):
    current_app.logger.debug("Entering method submit of user_dao.")
    db, connection = connection_manager.get_connection()
    fltr = {"tpid": tpid, "uid": uid}
    data = {"$set": {"completed": "y"}}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager.close_connection(connection)
    current_app.logger.debug("Entering method exit of user_dao.")


def update_responce(user_id, tpid, data):
    current_app.logger.debug("Entering method get_responce of user_dao.")
    db, connection = connection_manager.get_connection()
    fltr = {"tpid": tpid, "user_id": user_id}
    data = {"$set": {str(data['question_no']): data}}
    result = db.tp_usr.update_one(fltr, data)
    connection_manager.close_connection(connection)
    current_app.logger.debug("Exit method get_responce of user_dao.")


def get_responce(user_id, tpid, data):
    current_app.logger.debug("Entering method get_responce of user_dao.")
    db, connection = connection_manager.get_connection()
    fltr = {"tpid": tpid, "user_id": user_id}
    result = db.tp_usr.find_one(fltr)
    connection_manager.close_connection(connection)
    current_app.logger.debug("Exit method get_responce of user_dao.")
    result['_id'] = str(result['_id'])
    return result


def review(user_id, tpid):
    current_app.logger.debug("Entering method get_tp_by_id of test_paper_dao.")
    db, connection = connection_manager.get_connection()
    result = db.tp.find_one({"tpid": tpid, "user_id": user_id})
    connection_manager.close_connection(connection)
    current_app.logger.debug("Exit method get_tp_by_id of test_paper_dao.")
    result['_id'] = str(result['_id'])
    return result
