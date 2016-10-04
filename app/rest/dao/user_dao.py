from flask import current_app
import rest.dao.mongodb as connection_manager_mongo
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util
from bson.objectid import ObjectId


def change_password(data):
    current_app.logger.debug("Entering method change_password of user_dao.")
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "update secret set secret = %s, updated_date = %s, updated_by = %s where uid = %s"
        current_ts = util.get_current_ts()
        print(current_ts)
        data = (data['secret'], current_ts, data['access_token'], data['uid'])
        cursor.execute(sql, data)
        db.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return -1
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exit method change_password of user_dao.")
    return 1


def change_username(data):
    current_app.logger.debug("Entering method change_username of user_dao.")
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "update usr set username = %s, updated_date = %s, updated_by = %s where uid = %s"
        current_ts = util.get_current_ts()
        print(current_ts)
        dbdata = (data['new_username'], current_ts, data['access_token'], data['uid'])
        cursor.execute(sql, dbdata)
        db.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return -1
    finally:
        connection_manager_mysql.close_db(db)
    # updating username to mongo
    db, connection = connection_manager_mongo.get_connection()
    key = {"uid": data['uid']}
    data = {"username": data['new_username'], "uid": data['uid']}
    result = db.usr.update(key, data, upsert=True)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method change_username of user_dao.")
    return 1


def get_role_for_user(uid):
    current_app.logger.debug("Entering method get_role_for_user of user_dao")
    roles_list = list()
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "select usr_role.uid, usr_role.role_id, role.name  from usr_role, role where usr_role.role_id = role.role_id and  usr_role.uid = %s"
        data = (uid,)
        cursor.execute(sql, data)
        results = cursor.fetchall()
        for row in results:
            roles_list.append(row[2])
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return -1, roles_list
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Entering method get_role_for_user of user_dao")
    return 1, roles_list


def update_my_profile(data):
    current_app.logger.debug("Entering method update_my_profile of user_dao")
    db, connection = connection_manager_mongo.get_connection()
    key = {'uid': data['uid']}
    del data['access_token']
    result = db.usr.update(key, data, upsert=True)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method update_my_profile of user_dao")


def get_my_profile(uid):
    current_app.logger.debug("Entering method get_my_profile of user_dao")
    db, connection = connection_manager_mongo.get_connection()
    result = db.usr.find_one({"uid": uid})
    if result is not None:
        result['_id'] = str(result['_id'])
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exit method get_my_profile of user_dao")
    return result
