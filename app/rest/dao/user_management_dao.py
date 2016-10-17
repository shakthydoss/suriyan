from flask import current_app
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util
import requests
import json


def add_user(data):
    current_app.logger.debug("Entering method add_user of user_management_dao.")
    headers = {'content-type' : 'application/json'}
    r = requests.post('http://localhost/auth/addUser/', data=json.dumps(data), headers=headers)
    current_app.logger.debug("Exit method add_user of user_management_dao.")
    db = connection_manager_mysql.get_connection()
    cursor = db.cursor()
    if r.status_code == 200 or r.status_code == 201:
        return_data = json.loads(r.content)
        try:
            sql = "insert into usr (uid, username, updated_by) values ( %s, %s, %s);"
            values = (return_data["data"]["uid"], data["username"], data["updated_by"])
            cursor.execute(sql,values)
            db.commit()
        except Exception, e:
            current_app.logger.error("Exception : %s", e)
            db.rollback()
        finally:
            connection_manager_mysql.close_db(db)
    return r.content


def add_role(data):
    current_app.logger.debug("Entering method add_role of user_management_dao.")
    db = connection_manager_mysql.get_connection()
    cursor = db.cursor()
    role_ids = data['role_ids']
    try:
        # delete all current role.
        sql = "delete from usr_role where uid = %s;"
        cursor.execute(sql, (data['uid'],))
        for role_id in role_ids:
            # assign new role.
            sql = "insert into usr_role (uid, role_id, updated_by) values ( %s, %s, %s);"
            cursor.execute(sql, (data['uid'], role_id, data['updated_by'],))
        db.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        db.rollback()
        # something unexpected happed.
        return_value = -1
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exit method add_role of user_management_dao.")
