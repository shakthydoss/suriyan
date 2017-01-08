import json

import rest.dao.mongodb as connection_manager_mongo
import rest.utils.util as util
from bson.json_util import dumps
from flask import current_app


def add_role(data):
    current_app.logger.debug("Entering method add_user of user_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    role_id = util.get_key()
    val = {
        "role_id": role_id,
        "name": data["name"] if "name" in data else "",
        "description": data["description"] if "description" in data else "",
        "permission": data["permission"] if "permission" in data else [],
        "is_active": data["is_active"] if "is_active" in data else ""
    }
    db.role.insert(val)
    return role_id


def edit_role(data):
    current_app.logger.debug("Entering method edit_role of role_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {
        "role_id": data["role_id"]
    }
    val = {
        "$set": {
            "name": data["name"] if "name" in data else "",
            "description": data["description"] if "description" in data else "",
            "permission": data["permission"] if "permission" in data else [],
            "is_active": data["is_active"] if "is_active" in data else ""
        }
    }
    db.role.update(fltr, val)
    current_app.logger.debug("Entering method edit_role of role_management_dao")
    return 0


def get_all_roles():
    current_app.logger.debug("Entering method get_all_roles of role_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    result = json.loads(dumps(db.role.find()))
    current_app.logger.debug("Entering method get_all_roles of role_management_dao")
    return result


def get_role_by_id(role_id):
    current_app.logger.debug("Entering method get_role_by_id of role_management_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {
        "role_id": role_id
    }
    result = json.loads(dumps(db.role.find(fltr)))
    current_app.logger.debug("Entering method get_role_by_id of role_management_dao")
    return result
