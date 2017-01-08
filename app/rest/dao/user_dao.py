import json

import requests
import rest.dao.mongodb as connection_manager_mongo
import rest.dao.mysqldb as connection_manager_mysql
from flask import current_app


def change_password(data):
    current_app.logger.debug("Entering method change_password of user_dao.")
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost/auth/updatePassword/', data=json.dumps(data), headers=headers)
    current_app.logger.debug("Exit method change_password of user_dao.")
    return r.content


def change_username(data):
    current_app.logger.debug("Entering method change_username of user_dao.")
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost/auth/updateUsername/', data=json.dumps(data), headers=headers)
    print r.content
    return_value = None
    if r.status_code == 200 or r.status_code == 201:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        try:
            sql = "update usr set username = %s where uid = %s"
            values = (data["new_username"], data["uid"])
            cursor.execute(sql, values)
            db.commit()
            return_value = 1
            # TODO update username in mongodb
        except Exception, e:
            current_app.logger.error("Exception : %s", str(e))
            db.rollback()
            return_value = -1
        finally:
            connection_manager_mysql.close_db(db)
    else:
        return_value = -1
    current_app.logger.debug("Exit method change_username of user_dao.")
    return return_value


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
    del data["uid"]
    if data:
        val = {
            "$set": {
                "full_name": data["full_name"] if "full_name" in data else "",
                "email": data["email"] if "email" in data else "",
                "mobile": data["mobile"] if "mobile" in data else ""
            }
        }
        print json.dumps(val)
        result = db.usr.update(key, val, upsert=True)
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
