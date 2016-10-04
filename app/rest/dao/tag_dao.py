from flask import current_app
import rest.dao.mongodb as connection_manager_mongo
import rest.dao.mysqldb as connection_manager_mysql
import rest.utils.util as util
from bson.objectid import ObjectId


def get_tags():
    current_app.logger.debug("Entering method get_tags of tag_dao")
    tag_list = list()
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "select t.tag_id, t.name, t.description, t.is_active, u.username from tag t, usr u where t.updated_by = u.uid"
        cursor.execute(sql)
        columns = cursor.description
        results = cursor.fetchall()
        for value in results:
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            tag_list.append(tmp)
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return None
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exiting method get_tags of tag_dao")
    return tag_list


def get_tag_by_id(tag_id):
    current_app.logger.debug("Entering method get_tag_by_id of tag_dao")
    tag_list = list()
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "select tag_id, name, description, is_active from tag where tag_id = %s"
        data = (tag_id)
        cursor.execute(sql, data)
        columns = cursor.description
        results = cursor.fetchall()
        for value in results:
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            tag_list.append(tmp)
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return None
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exiting method get_tag_by_id of tag_dao")
    return tag_list


def save_tag(data):
    current_app.logger.debug("Entering method save_tag of tag_dao")
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "insert into tag (name, description, is_active, updated_by) values (%s, %s, %s, %s)"
        data = (data['name'], data['description'], data['is_active'], data['access_token'])
        cursor.execute(sql, data)
        db.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return -1
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exiting method save_tag of tag_dao")
    return 0;


def update_tag(data):
    current_app.logger.debug("Entering method update_tag of tag_dao")
    try:
        db = connection_manager_mysql.get_connection()
        cursor = db.cursor()
        sql = "update tag set name = %s, description = %s, is_active = %s, updated_date = %s, updated_by = %s where tag_id = %s"
        current_ts = util.get_current_ts()
        print(current_ts)
        data = (data['name'], data['description'], data['is_active'], current_ts, data['access_token'], data['tag_id'])
        cursor.execute(sql, data)
        db.commit()
    except Exception, e:
        current_app.logger.error("Exception : %s", e)
        return -1
    finally:
        connection_manager_mysql.close_db(db)
    current_app.logger.debug("Exiting method update_tag of tag_dao")
    return 0;


def delete_tag():
    return 0;
