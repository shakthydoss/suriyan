import json

import rest.dao.mongodb as connection_manager_mongo
import rest.utils.util as util
from bson.json_util import dumps
from flask import current_app


def add_user(data):
    current_app.logger.debug("Entering method add_user of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    uid = util.get_key()
    val = {
        "uid": uid,
        "username": data["username"] if "username" in data else "",
        "email": data["email"] if "email" in data else "",
        "full_name": data["full_name"] if "full_name" in data else "",
        "role": data["role"] if "role" in data else "",
        "is_active": data["is_active"] if "is_active" in data else "",
        "tags": data["tags"] if "tags" in data else "",
        "mobile": data["mobile"] if "mobile" in data else ""
    }
    db.usr.insert(val)
    val = {
        "uid": uid,
        "password": data["password"]
    }
    db.secret.insert(val)
    current_app.logger.debug("Exiting method add_user of user_management_dao")
    return uid


def edit_user(data):
    current_app.logger.debug("Entering method add_user of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {
        "uid": data["uid"]
    }
    val = {
        "$set": {
            "username": data["username"] if "username" in data else "",
            "email": data["email"] if "email" in data else "",
            "role": data["role"] if "role" in data else "",
            "is_active": data["is_active"] if "is_active" in data else "",
            "tags": data["tags"] if "tags" in data else "",
            "mobile": data["mobile"] if "mobile" in data else ""
        }
    }
    db.usr.update(fltr, val)
    current_app.logger.debug("Exiting method add_user of user_management_dao")
    return 0


def get_all_urs():
    current_app.logger.debug("Entering method get_all_users of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    result = json.loads(dumps(db.usr.find()))
    current_app.logger.debug("Exiting method get_all_users of user_management_dao")
    return result


def get_usr_by(uid):
    current_app.logger.debug("Entering method get_usr_by of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {
        "uid": uid
    }
    result = json.loads(dumps(db.usr.find(fltr)))
    current_app.logger.debug("Exiting method get_usr_by of user_management_dao")
    return result


def reset_password(data):
    current_app.logger.debug("Entering method reset_password of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {
        "uid": data["uid"]
    }
    val = {
        "$set": {
            "password": data["password"]
        }
    }
    db.secret.update(fltr, val)
    current_app.logger.debug("Exiting method reset_password of user_management_dao")
    return 0
